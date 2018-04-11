# -*- coding: utf-8 -*-

from support_funcs import *


# Xpaths

# Logo - taki sam xpath na kazdej stronie
__admin_logo = "//*[@id='content']/div/div/h1"

# Tabela - taki sam xpath na kazdej stronie
__admin_tabela = "//*[@id='widget-grid']/div[2]/article/div[1]/table"

# Tabela ustawienia
__admin_ustawienia_tabela = "//*[@id='wid-id-application_settings']/header"

# Admin button
__admin_button = "//*[@id='left-panel']/nav/ul/li[4]/a"

# Role button
__admin_role_button = "//*[@id='left-panel']/nav/ul/li[4]/ul/li[1]/a"

# Uprawnienia button
__admin_uprawnienia_button = "//*[@id='left-panel']/nav/ul/li[4]/ul/li[2]/a"

# Uzytkownicy button
__admin_uzytkownicy_button = "//*[@id='left-panel']/nav/ul/li[4]/ul/li[3]/a"

# Strony button
__admin_strony_button = "//*[@id='left-panel']/nav/ul/li[4]/ul/li[4]/a"

# Ustawienia button
__admin_ustawienia_button = "//*[@id='left-panel']/nav/ul/li[4]/ul/li[5]/a"

# Log out button
__log_out_button = "//*[@id='logout']/span/a"

def hit_enter_on_admin_button(driver_instance):
    click_enter_on_element(
        driver_instance = driver_instance,
        xpath = __admin_button
    )

def check_hitting_results_are_correct_role(driver_instance, text):
    elem = wait_for_visibility_of_element(
        driver_instance=driver_instance,
        xpath=__admin_role_button
    )
    elem_text = elem.text
    return elem_text == text

def hit_enter_on_admin_role_button(driver_instance):
    click_enter_on_element(
        driver_instance = driver_instance,
        xpath = __admin_role_button
    )

def check_admin_logo(driver_instance, text):
    elem = wait_for_visibility_of_element(
        driver_instance=driver_instance,
        xpath=__admin_logo
    )
    elem_text = elem.text
    return elem_text == text

def check_admin_tabela(driver_instance):
    elem = wait_for_visibility_of_element(
        driver_instance=driver_instance,
        xpath=__admin_tabela
    )
    return elem

def hit_enter_on_admin_uprawnienia_button(driver_instance):
    click_enter_on_element(
        driver_instance = driver_instance,
        xpath = __admin_uprawnienia_button
    )

def hit_enter_on_admin_uzytkownicy_button(driver_instance):
    click_enter_on_element(
        driver_instance = driver_instance,
        xpath = __admin_uzytkownicy_button
    )

def hit_enter_on_admin_strony_button(driver_instance):
    click_enter_on_element(
        driver_instance = driver_instance,
        xpath = __admin_strony_button
    )

def hit_enter_on_admin_ustawienia_button(driver_instance):
    click_enter_on_element(
        driver_instance = driver_instance,
        xpath = __admin_ustawienia_button
    )

def check_admin_ustawienia_tabela(driver_instance):
    elem = wait_for_visibility_of_element(
        driver_instance=driver_instance,
        xpath=__admin_ustawienia_tabela
    )
    return elem

def hit_enter_on_log_out_button(driver_instance):
    click_enter_on_element(
        driver_instance = driver_instance,
        xpath = __log_out_button
    )