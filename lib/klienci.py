# -*- coding: utf-8 -*-

from lib.funkcje_pomocnicze import *

# Xpaths

# Logo - taki sam xpath na kazdej stronie
__klienci_logo = "//*[@id='content']/div/div/h1"

# Tabela - taki sam xpath na kazdej stronie
__klienic_tabela = "//*[@id='widget-grid']/div[2]/article/div[1]/table"

# Oddzialy przycisk
__klienci_oddzialy_przycisk = "//*[@id='left-panel']/nav/ul/li[2]/ul/li[2]/a"

# Osoby kontaktowe przycisk
__klienci_osoby_kontaktowe_przycisk = "//*[@id='left-panel']/nav/ul/li[2]/ul/li[3]/a"

# Ostrzeżenia przycisk
__klienci_ostrzezenia_przycisk = "//*[@id='left-panel']/nav/ul/li[2]/ul/li[4]/a"

# Sekretariat przycisk w menu
__pulpit_sekretariat_przycisk_xpath = "//*[@id='left-panel']/nav/ul/li[3]/a/span"
__pulpit_sekretariat_xpath = "//*[@id='left-panel']/nav/ul/li[3]/a"


def sprawdz_klienci_logo(driver_instance, text):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__klienci_logo
    )
    elem_text = elem.text
    return elem_text == text


def sprawdz_klienci_tabela(driver_instance):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__klienic_tabela
    )
    return elem


def nacisnij_enter_na_oddzialy_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__klienci_oddzialy_przycisk
    )


def nacisnij_enter_na_osoby_kontaktowe_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__klienci_osoby_kontaktowe_przycisk
    )


def nacisnij_enter_na_ostrzezenia_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__klienci_ostrzezenia_przycisk
    )
