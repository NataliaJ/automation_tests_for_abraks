# -*- coding: utf-8 -*-

from lib.funkcje_pomocnicze import *

# Xpaths

# Top logo bar
__top_logo_bar_xpath = "//*[@id='logo']/img"

# Login section
__login_section_xpath = "//*[@id='login-form']"

# Email field
__email_field_xpath = "//*[@id='email']"

# Password field
__password_field_xpath = "//*[@id='password']"

# Logging button
__login_button_xpath = "//*[@id='login-form']/footer/button"


def login(test, driver_instance):
    input_text = "tester@abraks.pl"
    input_text2 = "Rety$675"

    test.assertTrue(check_top_logo_bar_is_visible(driver_instance))
    input_email_to_email_field(driver_instance, input_text)
    input_password_to_password_field(driver_instance, input_text2)
    hit_enter_on_logging_button(driver_instance)


def check_top_logo_bar_is_visible(driver_instance):
    elem = wait_for_visibility_of_element(
        driver_instance=driver_instance,
        xpath=__top_logo_bar_xpath
    )
    return elem.is_displayed()


def check_loging_section_is_visible(driver_instance):
    elem = wait_for_visibility_of_element(
        driver_instance=driver_instance,
        xpath=__login_section_xpath
    )
    return elem.is_displayed()


def input_email_to_email_field(driver_instance, text):
    send_keys_to_element(
        driver_instance=driver_instance,
        xpath=__email_field_xpath,
        text=text
    )


def input_password_to_password_field(driver_instance, text):
    send_keys_to_element(
        driver_instance=driver_instance,
        xpath=__password_field_xpath,
        text=text
    )


def hit_enter_on_logging_button(driver_instance):
    click_enter_on_element(
        driver_instance=driver_instance,
        xpath=__login_button_xpath
    )
