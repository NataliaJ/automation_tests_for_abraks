# -*- coding: utf-8 -*-

from Funkcje.funkcje_pomocnicze import *

# Xpaths

# Logo - taki sam xpath na kazdej stronie
__admin_logo = "//*[@id='content']/div/div/h1"

# Tabela - taki sam xpath na kazdej stronie
__admin_tabela = "//*[@id='widget-grid']/div[2]/article/div[1]/table"

# Tabela ustawienia aplikacji
__admin_ustawienia_aplikacji_tabela = "//*[@id='wid-id-application_settings']/header"

# Tabela ustawienia firmy
__admin_ustawienia_firmy_tabela = "//*[@id='wid-id-company_settings']/header"

# Tabela ustawienia sekcji Meta
__admin_ustawienia_sekcji_meta_tabela = "//*[@id='wid-id-meta_settings']/header"

# Admin przycisk
__admin_przycisk = "//*[@id='left-panel']/nav/ul/li[4]/a"

# Role przycisk
__admin_role_przycisk = "//*[@id='left-panel']/nav/ul/li[4]/ul/li[1]/a"

# Uprawnienia przycisk
__admin_uprawnienia_przycisk = "//*[@id='left-panel']/nav/ul/li[4]/ul/li[2]/a"

# Uzytkownicy przycisk
__admin_uzytkownicy_przycisk = "//*[@id='left-panel']/nav/ul/li[4]/ul/li[3]/a"

# Strony przycisk
__admin_strony_przycisk = "//*[@id='left-panel']/nav/ul/li[4]/ul/li[4]/a"

# Ustawienia przycisk
__admin_ustawienia_przycisk = "//*[@id='left-panel']/nav/ul/li[4]/ul/li[5]/a"


def nacisnij_enter_na_admin_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__admin_przycisk
    )


def sprawdz_rezultat_nacisniecia_role(driver_instance, text):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__admin_role_przycisk
    )
    elem_text = elem.text
    return elem_text == text


def nacisnij_enter_na_role_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__admin_role_przycisk
    )


def sprawdz_admin_logo(driver_instance, text):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__admin_logo
    )
    elem_text = elem.text
    return elem_text == text


def sprawdz_admin_tabela(driver_instance):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__admin_tabela
    )
    return elem


def nacisnij_enter_na_admin_uprawnienia_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__admin_uprawnienia_przycisk
    )


def nacisnij_enter_na_admin_uzytkownicy_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__admin_uzytkownicy_przycisk
    )


def nacisnij_enter_na_admin_strony_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__admin_strony_przycisk
    )


def nacisnij_enter_na_admin_ustawienia_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__admin_ustawienia_przycisk
    )


def sprawdz_admin_ustawienia_aplikacji_tabela(driver_instance):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__admin_ustawienia_aplikacji_tabela
    )
    return elem

def sprawdz_admin_ustawienia_firmy_tabela(driver_instance):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__admin_ustawienia_firmy_tabela
    )
    return elem

def sprawdz_admin_ustawienia_sekcji_meta_tabela(driver_instance):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__admin_ustawienia_sekcji_meta_tabela
    )
    return elem

