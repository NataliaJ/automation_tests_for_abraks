# -*- coding: utf-8 -*-

from support_funcs import *


# Xpaths

# Logging result, Pulpit is visible
__pulpit_logo_xpath = "//*[@id='content']/div/div/h1"

# Klienci button in menu
__pulpit_klienci_button_xpath = "//*[@id='left-panel']/nav/ul/li[2]/a/span"
__pulpit_klienci_xpath = "//*[@id='left-panel']/nav/ul/li[2]/a"

# Kontrahenci button in menu
__pulpit_kontrahenci_button_xpath = "//*[@id='left-panel']/nav/ul/li[2]/ul/li[1]/a"

# Widgety na pulpicie
__pulpit_widget_xpath = "//*[@id='widget-grid']/div[2]/article"

def check_loging_results_are_correct(driver_instance, text):
    elem = wait_for_visibility_of_element_after_login(
        driver_instance=driver_instance,
        xpath=__pulpit_logo_xpath
    )
    elem_text = elem.text
    print(elem_text)
    return elem_text == text

def check_loging_results_are_correct_klinci(driver_instance, text):
    elem = wait_for_visibility_of_element_after_login(
        driver_instance=driver_instance,
        xpath=__pulpit_klienci_button_xpath
    )
    elem_text = elem.text
    print(elem_text)
    return elem_text == text

def hit_enter_on_klienci_button(driver_instance):
    click_enter_on_element(
        driver_instance=driver_instance,
        xpath=__pulpit_klienci_xpath
    )

def check_hitting_results_are_correct_kontrahenci(driver_instance, text):
    elem = wait_for_visibility_of_element(
        driver_instance=driver_instance,
        xpath=__pulpit_kontrahenci_button_xpath
    )
    elem_text = elem.text
    print(elem_text)
    return elem_text == text

def hit_enter_on_kontrahenci_button(driver_instance):
    click_enter_on_element(
        driver_instance=driver_instance,
        xpath=__pulpit_kontrahenci_button_xpath
    )