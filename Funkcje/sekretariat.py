# -*- coding: utf-8 -*-

from Funkcje.funkcje_pomocnicze import *

# Xpaths

# Logo - taki sam xpath na kazdej stronie
__sekretariat_logo = "//*[@id='content']/div/div/h1"

# Tabela - taki sam xpath na kazdej stronie
__sekretariat_tabela = "//*[@id='widget-grid']/div[2]/article/div[1]/table"

# Sekretariat button
__sekretariat_button = "//*[@id='left-panel']/nav/ul/li[3]/a"

# Dokumenty przycisk
__sekretariat_dokumenty_przycisk = "//*[@id='left-panel']/nav/ul/li[3]/ul/li[1]/a"

# Sprawy przycisk
__sekretariat_sprawy_przycisk = "//*[@id='left-panel']/nav/ul/li[3]/ul/li[2]/a"

# Tematy przycisk
__sekretariat_tematy_przycisk = "//*[@id='left-panel']/nav/ul/li[3]/ul/li[3]/a"

# Ksiazki listowe
__sekretariat_ksiazki_listowe_przycisk = "//*[@id='left-panel']/nav/ul/li[3]/ul/li[4]/a"

# Pisma przychodzace
__sekretariat_pisma_przychodzace_przycisk = "//*[@id='left-panel']/nav/ul/li[3]/ul/li[5]/a"

# Pisma wychodzace
__sekretariat_pisma_wychodzace_przycisk = "//*[@id='left-panel']/nav/ul/li[3]/ul/li[6]/a"

# Urlopy przycisk
__sekretariat_urlopy_przycisk = "//*[@id='left-panel']/nav/ul/li[3]/ul/li[7]/a"

# Zadania przycisk
__sekretariat_zadania_przycisk = "//*[@id='left-panel']/nav/ul/li[3]/ul/li[8]/a"


def nacisnij_enter_na_sekretariat_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__sekretariat_button
    )


def check_hitting_results_are_correct_dokumenty(driver_instance, text):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__sekretariat_dokumenty_przycisk
    )
    elem_text = elem.text
    return elem_text == text


def nacisnij_enter_na_sekretariat_dokumenty_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__sekretariat_dokumenty_przycisk
    )


def sprawdz_sekretariat_logo(driver_instance, text):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__sekretariat_logo
    )
    elem_text = elem.text
    return elem_text == text


def sprawdz_sekretariat_tabela(driver_instance):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__sekretariat_tabela
    )
    return elem


def nacisnij_enter_na_sekretariat_sprawy_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__sekretariat_sprawy_przycisk
    )


def nacisnij_enter_na_sekretariat_tematy_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__sekretariat_tematy_przycisk
    )


def nacisnij_enter_na_sekretariat_ksiazki_listow_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__sekretariat_ksiazki_listowe_przycisk
    )


def nacisnij_enter_na_sekretariat_pisma_przychodzace_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__sekretariat_pisma_przychodzace_przycisk
    )


def nacisnij_enter_na_sekretariat_pisma_wychodzace_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__sekretariat_pisma_wychodzace_przycisk
    )


def nacisnij_enter_na_sekretariat_urlopy_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__sekretariat_urlopy_przycisk
    )


def nacisnij_enter_na_sekretariat_zadania_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__sekretariat_zadania_przycisk
    )
