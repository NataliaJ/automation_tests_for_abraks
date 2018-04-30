# -*- coding: utf-8 -*-

from lib.funkcje_pomocnicze import *

# Xpaths

# Logging result, Pulpit is visible
__pulpit_logo_xpath = "//*[@id='content']/div/div/h1"

# Admin button in menu
__pulpit_admin_button_xpath = "//*[@id='left-panel']/nav/ul/li[4]/a/span"
__pulpit_admin_xpath = "//*[@id='left-panel']/nav/ul/li[4]/a"

# Uzytkownicy button in menu
__pulpit_uzytkownicy_button_xpath = "//*[@id='left-panel']/nav/ul/li[4]/ul/li[3]/a"

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
    return elem_text == text


def check_loging_results_are_correct_admin(driver_instance, text):
    elem = wait_for_visibility_of_element_after_login(
        driver_instance=driver_instance,
        xpath=__pulpit_admin_button_xpath
    )
    elem_text = elem.text
    return elem_text == text


def hit_enter_on_admin_button(driver_instance):
    click_enter_on_element(
        driver_instance=driver_instance,
        xpath=__pulpit_admin_xpath
    )


def check_hitting_results_are_correct_uzytkownicy(driver_instance, text):
    elem = wait_for_visibility_of_element(
        driver_instance=driver_instance,
        xpath=__pulpit_uzytkownicy_button_xpath
    )
    elem_text = elem.text
    return elem_text == text


def hit_enter_on_uzytkownicy_button(driver_instance):
    click_enter_on_element(
        driver_instance=driver_instance,
        xpath=__pulpit_uzytkownicy_button_xpath
    )

def check_loging_results_are_correct_klinci(driver_instance, text):
    elem = wait_for_visibility_of_element_after_login(
        driver_instance=driver_instance,
        xpath=__pulpit_klienci_button_xpath
    )
    elem_text = elem.text
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
    return elem_text == text


def hit_enter_on_kontrahenci_button(driver_instance):
    click_enter_on_element(
        driver_instance=driver_instance,
        xpath=__pulpit_kontrahenci_button_xpath
    )
