# -*- coding: utf-8 -*-

from support_funcs import *


# Xpaths

# Logo Uzytkownik
__uzytkownik_logo = "//*[@id='content']/div/div/h1"

# Tabela
__uzytkownik_tabela = "//*[@id='widget-grid']/div[2]/article/div[1]/table"

# Szukaj
__szukaj_xpath = "//*[@id='search_box']"

# Per page
__per_page = "//*[@id='perpage']/option[1]"

# Dodaj button
__dodaj_button = "//*[@id='dt_basic_filter']/a"

# Jezyk filtr
__jezyk_filtr = "//*[@id='language']"

# Aktywny filtr
__aktywny_filtr = "//*[@id='active']"

# Regulamin zaakceptowany filtr
__regulamin_zaakceptowany_filtr = "//*[@id='terms']"

# Typ Uzytkuwnika
__typ_uzytkownika_filtr = "//*[@id='type']"


def check_uzytkownik_logo(driver_instance, text):
    elem = wait_for_visibility_of_element(
        driver_instance=driver_instance,
        xpath=__uzytkownik_logo
    )
    elem_text = elem.text
    print(elem_text)
    return elem_text == text

def check_uzytkownik_tabela(driver_instance):
    elem = wait_for_visibility_of_element(
        driver_instance=driver_instance,
        xpath=__uzytkownik_tabela
    )
    return elem

def check_uzytkownik_szukaj(driver_instance):
    elem = wait_for_visibility_of_element(
        driver_instance = driver_instance,
        xpath = __szukaj_xpath
    )
    return elem

def check_uzytkownik_per_page(driver_instance):
    elem = wait_for_visibility_of_element(
        driver_instance = driver_instance,
        xpath = __per_page
    )
    return elem

def check_uzytkownik_dodaj_button(driver_instance):
    elem = wait_for_visibility_of_element(
        driver_instance = driver_instance,
        xpath = __dodaj_button
    )
    return elem

def check_uzytkownik_jezyk_filtr(driver_instance):
    elem = wait_for_visibility_of_element(
        driver_instance = driver_instance,
        xpath = __jezyk_filtr
    )
    return elem

def check_uzytkownik_aktywny_filtr(driver_instance):
    elem = wait_for_visibility_of_element(
        driver_instance = driver_instance,
        xpath = __aktywny_filtr
    )
    return elem

def check_uzytkownik_regulamin_zaakceptowany_filtr(driver_instance):
    elem = wait_for_visibility_of_element(
        driver_instance = driver_instance,
        xpath = __regulamin_zaakceptowany_filtr
    )
    return elem

def check_uzytkownik_typ_uzytkownika_filtr(driver_instance):
    elem = wait_for_visibility_of_element(
        driver_instance = driver_instance,
        xpath = __typ_uzytkownika_filtr
    )
    print('wszystko super :D')
    return elem