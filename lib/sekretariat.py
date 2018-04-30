# -*- coding: utf-8 -*-

from lib.funkcje_pomocnicze import *

# Xpaths

# Logo - taki sam xpath na kazdej stronie
__sekretariat_logo = "//*[@id='content']/div/div/h1"

# Tabela - taki sam xpath na kazdej stronie
__sekretariat_tabela = "//*[@id='widget-grid']/div[2]/article/div[1]/table"

# Sekretariat button
__sekretariat_button = "//*[@id='left-panel']/nav/ul/li[3]/a"

# Dokumenty button
__sekretariat_dokumenty_button = "//*[@id='left-panel']/nav/ul/li[3]/ul/li[1]/a"

# Sprawy button
__sekretariat_sprawy_button = "//*[@id='left-panel']/nav/ul/li[3]/ul/li[2]/a"

# Tematy button
__sekretariat_tematy_button = "//*[@id='left-panel']/nav/ul/li[3]/ul/li[3]/a"

# Ksiazki listowe
__sekretariat_ksiazki_listowe_button = "//*[@id='left-panel']/nav/ul/li[3]/ul/li[4]/a"

# Pisma przychodzace
__sekretariat_pisma_przychodzace_button = "//*[@id='left-panel']/nav/ul/li[3]/ul/li[5]/a"

# Pisma wychodzace
__sekretariat_pisma_wychodzace_button = "//*[@id='left-panel']/nav/ul/li[3]/ul/li[6]/a"

# Urlopy button
__sekretariat_urlopy_button = "//*[@id='left-panel']/nav/ul/li[3]/ul/li[7]/a"

# Zadania button
__sekretariat_zadania_button = "//*[@id='left-panel']/nav/ul/li[3]/ul/li[8]/a"


def hit_enter_on_sekretariat_button(driver_instance):
    click_enter_on_element(
        driver_instance=driver_instance,
        xpath=__sekretariat_button
    )


def check_hitting_results_are_correct_dokumenty(driver_instance, text):
    elem = wait_for_visibility_of_element(
        driver_instance=driver_instance,
        xpath=__sekretariat_dokumenty_button
    )
    elem_text = elem.text
    return elem_text == text


def hit_enter_on_sekretariat_dokumenty_button(driver_instance):
    click_enter_on_element(
        driver_instance=driver_instance,
        xpath=__sekretariat_dokumenty_button
    )


def check_sekretariat_logo(driver_instance, text):
    elem = wait_for_visibility_of_element(
        driver_instance=driver_instance,
        xpath=__sekretariat_logo
    )
    elem_text = elem.text
    return elem_text == text


def check_sekretariat_tabela(driver_instance):
    elem = wait_for_visibility_of_element(
        driver_instance=driver_instance,
        xpath=__sekretariat_tabela
    )
    return elem


def hit_enter_on_sekretariat_sprawy_button(driver_instance):
    click_enter_on_element(
        driver_instance=driver_instance,
        xpath=__sekretariat_sprawy_button
    )


def hit_enter_on_sekretariat_tematy_button(driver_instance):
    click_enter_on_element(
        driver_instance=driver_instance,
        xpath=__sekretariat_tematy_button
    )


def hit_enter_on_sekretariat_ksiazki_listow_button(driver_instance):
    click_enter_on_element(
        driver_instance=driver_instance,
        xpath=__sekretariat_ksiazki_listowe_button
    )


def hit_enter_on_sekretariat_pisma_przychodzace_button(driver_instance):
    click_enter_on_element(
        driver_instance=driver_instance,
        xpath=__sekretariat_pisma_przychodzace_button
    )


def hit_enter_on_sekretariat_pisma_wychodzace_button(driver_instance):
    click_enter_on_element(
        driver_instance=driver_instance,
        xpath=__sekretariat_pisma_wychodzace_button
    )


def hit_enter_on_sekretariat_urlopy_button(driver_instance):
    click_enter_on_element(
        driver_instance=driver_instance,
        xpath=__sekretariat_urlopy_button
    )


def hit_enter_on_sekretariat_zadania_button(driver_instance):
    click_enter_on_element(
        driver_instance=driver_instance,
        xpath=__sekretariat_zadania_button
    )
