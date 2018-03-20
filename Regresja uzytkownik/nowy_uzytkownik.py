# -*- coding: utf-8 -*-

from support_funcs import *


# Xpaths

# Logo Uzytkownik utworz
__logo_utworz_uzytkownik = "//*[@id='content']/div/div/h1"

# Anuluj button
__anuluj_button = "//*[@id='admin_user_manage']/footer/a"

#Dodaj Uzytkownika button
__dodaj_uzytkownika_button = "//*[@id='admin_user_manage']/footer/button"

#To pole jest wymagane
__to_pole_jest_wymagane = "//*[@id='username-error']"


def check_logo_utworz_uzytkownik(driver_instance, text):
    elem = wait_for_visibility_of_element(
        driver_instance=driver_instance,
        xpath=__logo_utworz_uzytkownik
    )
    elem_text = elem.text
    print(elem_text)
    return elem_text == text

def check_anuluj_button(driver_instance):
    elem = wait_for_visibility_of_element(
        driver_instance=driver_instance,
        xpath=__anuluj_button
    )
    return elem

def check_dodaj_uzytkownik_button(driver_instance):
    elem = wait_for_visibility_of_element(
        driver_instance=driver_instance,
        xpath=__dodaj_uzytkownika_button
    )
    return elem

def check_to_pole_jest_wymagane(driver_instance):
    elem = wait_for_visibility_of_element(
        driver_instance=driver_instance,
        xpath=__to_pole_jest_wymagane
    )
    return elem

def hit_enter_on_anuluj_button(driver_instance):
    click_enter_on_element(
        driver_instance = driver_instance,
        xpath= __anuluj_button
    )

def hit_enter_on_dodaj_uzytkownik_button(driver_instance):
    click_enter_on_element(
        driver_instance = driver_instance,
        xpath= __dodaj_uzytkownika_button
    )