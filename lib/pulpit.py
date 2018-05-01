# -*- coding: utf-8 -*-

from lib.funkcje_pomocnicze import *

# Xpaths

# Logo strony
__pulpit_logo_strony_xpath = "//*[@id='logo']/img"

# Logo pulpitu
__pulpit_logo_xpath = "//*[@id='content']/div/div/h1"

# Admin przycisk
__pulpit_admin_przycisk_xpath = "//*[@id='left-panel']/nav/ul/li[4]/a/span"
__pulpit_admin_xpath = "//*[@id='left-panel']/nav/ul/li[4]/a"

# Uzytkownicy przycisk
__pulpit_uzytkownicy_przycisk_xpath = "//*[@id='left-panel']/nav/ul/li[4]/ul/li[3]/a"

# Klienci przycisk
__pulpit_klienci_przycisk_xpath = "//*[@id='left-panel']/nav/ul/li[2]/a/span"
__pulpit_klienci_xpath = "//*[@id='left-panel']/nav/ul/li[2]/a"

# Kontrahenci przycisk
__pulpit_kontrahenci_przycisk_xpath = "//*[@id='left-panel']/nav/ul/li[2]/ul/li[1]/a"

# Widzety na pulpicie
__pulpit_widzet_xpath = "//*[@id='widget-grid']/div[2]/article/article"

def sprawdz_poprawnosc_logowania_logo(driver_instance):
    elem = poczekaj_na_widocznosc_elementu_po_logowaniu(
        driver_instance=driver_instance,
        xpath=__pulpit_logo_strony_xpath
    )
    return elem

def sprawdz_poprawnosc_logowania(driver_instance, text):
    elem = poczekaj_na_widocznosc_elementu_po_logowaniu(
        driver_instance=driver_instance,
        xpath=__pulpit_logo_xpath
    )
    elem_text = elem.text
    return elem_text == text


def sprawdz_poprawnosc_logowania_admin(driver_instance, text):
    elem = poczekaj_na_widocznosc_elementu_po_logowaniu(
        driver_instance=driver_instance,
        xpath=__pulpit_admin_przycisk_xpath
    )
    elem_text = elem.text
    return elem_text == text


def nacisnij_enter_na_admin_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__pulpit_admin_xpath
    )


def sprawdz_poprawnosc_nacisniecia_uzytkownicy(driver_instance, text):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__pulpit_uzytkownicy_przycisk_xpath
    )
    elem_text = elem.text
    return elem_text == text


def nacisnij_enter_na_uzytkownicy_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__pulpit_uzytkownicy_przycisk_xpath
    )

def sprawdz_poprawnosc_logowania_klienci(driver_instance, text):
    elem = poczekaj_na_widocznosc_elementu_po_logowaniu(
        driver_instance=driver_instance,
        xpath=__pulpit_klienci_przycisk_xpath
    )
    elem_text = elem.text
    return elem_text == text


def nacisnij_enter_na_klienci_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__pulpit_klienci_xpath
    )


def sprawdz_poprawnosc_nacisniecia_kontrahenci(driver_instance, text):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__pulpit_kontrahenci_przycisk_xpath
    )
    elem_text = elem.text
    return elem_text == text


def nacisnij_enter_na_kontrahenci_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__pulpit_kontrahenci_przycisk_xpath
    )


def policz_widgety_w_tabeli(driver_instance):
    elems = poczekaj_na_widocznosc_wszystkich_elementow(
        driver_instance=driver_instance,
        xpath=__pulpit_widzet_xpath
    )
    return len(elems)