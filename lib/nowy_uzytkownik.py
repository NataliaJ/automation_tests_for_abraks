# -*- coding: utf-8 -*-

from lib.funkcje_pomocnicze import *

# Xpaths

# Logo Uzytkownik utworz
__logo_utworz_uzytkownik = "//*[@id='content']/div/div/h1"

# Anuluj button
__anuluj_button = "//*[@id='admin_user_manage']/footer/a"

# Dodaj Uzytkownika button
__dodaj_uzytkownika_button = "//*[@id='admin_user_manage']/footer/button"

# To pole jest wymagane
__to_pole_jest_wymagane = "//*[@id='username-error']"

# Pole Nazwa Uzytkownika
__nazwa_uzytkownika_xpath = "//*[@id='admin_user_manage']/fieldset[1]/div[2]/section[1]/label[2]/input"

# Pole Email
__email_xpath = "//*[@id='admin_user_manage']/fieldset[1]/div[2]/section[2]/label[2]/input"

# Pole Imie i Nazwisko
__imie_i_nazwisko_xpath = "//*[@id='admin_user_manage']/fieldset[1]/div[2]/section[3]/label[2]/input"

# Pole Telefon
__telefon_xpath = "//*[@id='admin_user_manage']/fieldset[2]/div/section[1]/label[2]/input"

# Jezyk
__jezyk_xpath = "//*[@id='language']"

# Jezyk Polski
__jezyk_polski_xpath = "//*[@id='language']/option[2]"

# Jezyk Angielski
__jezyk_angielski_xpath = "//*[@id='language']/option[3]"

# Aktywny
__aktywny_xpath = "//*[@id='active']"

# Aktywny Tak
__aktywny_tak_xpath = "//*[@id='active']/option[2]"

# Aktywny Nie
__aktywny_nie_xpath = "//*[@id='active']/option[3]"

# Regulamin Zaakceptowany
__regulamin_zaakceptowany_xpath = "//*[@id='terms']"

# Regulamin Zaakceptowany Tak
__regulamin_zaakceptowany_tak_xpath = "//*[@id='terms']/option[2]"

# Regulamin Zaakceptowany Nie
__regulamin_zaakceptowany_nie_xpath = "//*[@id='terms']/option[3]"

# Typ uzytkownika
__typ_uzytkownika = "//*[@id='type']"

# Typ uzytkownika wewnetrzny
__typ_uzytkownika_wewnetrzny = "//*[@id='type']/option[2]"

# Typ uzytkownika zewnetrzny
__typ_uzytkownika_zewnetrzny = "//*[@id='type']/option[2]"

# Typ uzytkownika wspolpracownik
__typ_uzytkownika_wspolpracownik = "//*[@id='type']/option[2]"

# Typ uzytkownika gosc
__typ_uzytkownika_gosc = "//*[@id='type']/option[2]"


def check_logo_utworz_uzytkownik(driver_instance, text):
    elem = wait_for_visibility_of_element(
        driver_instance=driver_instance,
        xpath=__logo_utworz_uzytkownik
    )
    elem_text = elem.text
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


def check_nazwa_uzytkownika_xpath(driver_instance):
    elem = wait_for_visibility_of_element(
        driver_instance=driver_instance,
        xpath=__nazwa_uzytkownika_xpath
    )
    return elem


def hit_enter_on_anuluj_button(driver_instance):
    click_enter_on_element(
        driver_instance=driver_instance,
        xpath=__anuluj_button
    )


def hit_enter_on_dodaj_uzytkownik_button(driver_instance):
    click_enter_on_element(
        driver_instance=driver_instance,
        xpath=__dodaj_uzytkownika_button
    )


def input_text_to_nazwa_uzytkownika_xpath(driver_instance, text):
    send_keys_to_element(
        driver_instance=driver_instance,
        xpath=__nazwa_uzytkownika_xpath,
        text=text
    )


def input_text_to_email_xpath(driver_instance, text):
    send_keys_to_element(
        driver_instance=driver_instance,
        xpath=__email_xpath,
        text=text
    )


def input_text_to_imie_i_nazwisko_xpath(driver_instance, text):
    send_keys_to_element(
        driver_instance=driver_instance,
        xpath=__imie_i_nazwisko_xpath,
        text=text
    )


def input_text_to_telefon_xpath(driver_instance, text):
    send_keys_to_element(
        driver_instance=driver_instance,
        xpath=__telefon_xpath,
        text=text
    )


def click_jezyk_polski_xpath(driver_instance):
    elem = wait_for_presence_of_element(
        driver_instance=driver_instance,
        xpath=__jezyk_polski_xpath
    )
    elem.click()


def click_jezyk_angielski_xpath(driver_instance):
    elem = wait_for_presence_of_element(
        driver_instance=driver_instance,
        xpath=__jezyk_angielski_xpath
    )
    elem.click()


def click_aktywny_tak_xpath(driver_instance):
    elem = wait_for_presence_of_element(
        driver_instance=driver_instance,
        xpath=__aktywny_tak_xpath
    )
    elem.click()


def click_aktywny_nie_xpath(driver_instance):
    elem = wait_for_presence_of_element(
        driver_instance=driver_instance,
        xpath=__aktywny_nie_xpath
    )
    elem.click()


def click_regulamin_zaakceptowany_tak_xpath(driver_instance):
    elem = wait_for_presence_of_element(
        driver_instance=driver_instance,
        xpath=__regulamin_zaakceptowany_tak_xpath
    )
    elem.click()


def click_regulamin_zaakceptowany_nie_xpath(driver_instance):
    elem = wait_for_presence_of_element(
        driver_instance=driver_instance,
        xpath=__regulamin_zaakceptowany_nie_xpath
    )
    elem.click()


def click_typ_uzytkownika_wewnetrzny(driver_instance):
    elem = wait_for_presence_of_element(
        driver_instance=driver_instance,
        xpath=__typ_uzytkownika_wewnetrzny
    )
    elem.click()


def click_typ_uzytkownika_zewnetrzny(driver_instance):
    elem = wait_for_presence_of_element(
        driver_instance=driver_instance,
        xpath=__typ_uzytkownika_zewnetrzny
    )
    elem.click()


def click_typ_uzytkownika_wspolpracownik(driver_instance):
    elem = wait_for_presence_of_element(
        driver_instance=driver_instance,
        xpath=__typ_uzytkownika_wspolpracownik
    )
    elem.click()


def click_typ_uzytkownika_gosc(driver_instance):
    elem = wait_for_presence_of_element(
        driver_instance=driver_instance,
        xpath=__typ_uzytkownika_gosc
    )
    elem.click()
