# -*- coding: utf-8 -*-

from support_funcs import *


# Xpaths

# Logo
__klienci_logo = "//*[@id='content']/div/div/h1"

# Tabela
__klienic_tabela = "//*[@id='widget-grid']/div[2]/article/div[1]/table"

# Oddzialy button
__klienci_oddzialy_button = "//*[@id='left-panel']/nav/ul/li[2]/ul/li[2]/a"

# Osoby kontaktowe button
__klienci_osoby_kontaktowe_button = "//*[@id='left-panel']/nav/ul/li[2]/ul/li[3]/a"

# Ostrzeżenia button
__klienci_ostrzezenia_button = "//*[@id='left-panel']/nav/ul/li[2]/ul/li[4]/a"

# Sekretariat button in menu
__pulpit_klienci_button_xpath = "//*[@id='left-panel']/nav/ul/li[2]/a/span"
__pulpit_klienci_xpath = "//*[@id='left-panel']/nav/ul/li[2]/a"

def check_klienci_logo(driver_instance, text):
    elem = wait_for_visibility_of_element(
        driver_instance=driver_instance,
        xpath=__klienci_logo
    )
    elem_text = elem.text
    print(elem_text)
    return elem_text == text

def check_klienci_tabela(driver_instance):
    elem = wait_for_visibility_of_element(
        driver_instance=driver_instance,
        xpath=__klienic_tabela
    )
    return elem

def hit_enter_on_oddzialy_button(driver_instance):
    click_enter_on_element(
        driver_instance=driver_instance,
        xpath=__klienci_oddzialy_button
    )

def hit_enter_on_osoby_kontaktowe_button(driver_instance):
    click_enter_on_element(
        driver_instance = driver_instance,
        xpath = __klienci_osoby_kontaktowe_button
    )

def hit_enter_on_ostrzezenia_button(driver_instance):
    click_enter_on_element(
        driver_instance = driver_instance,
        xpath = __klienci_ostrzezenia_button
    )