# -*- coding: utf-8 -*-

from Funkcje.funkcje_pomocnicze import *

# Xpaths

# Gorne logo pasek
__gorne_logo_pasek_xpath = "//*[@id='logo']/img"

# Sekcja Logowania
__sekcja_logowania_xpath = "//*[@id='login-form']"

# Email pole
__pole_email_xpath = "//*[@id='email']"

# Haslo pole
__pole_haslo_xpath = "//*[@id='password']"

# Przycisk logowania
__przycisk_logowania_xpath = "//*[@id='login-form']/footer/button"

# Wyloguj przycisk
__wyloguj_przycisk = "//*[@id='logout']/span/a"


def login(test, driver_instance):
    input_text = "tester@abraks.pl"
    input_text2 = "Rety$675"

    test.assertTrue(
        sprawdz_czy_gorne_logo_pasek_jest_widoczne(driver_instance)
    )
    test.assertTrue(
        sprawdz_czy_sekcja_logowania_jest_widoczna(driver_instance)
    )
    wprowadz_email_do_pole_email(driver_instance, input_text)
    wprowadz_haslo_do_pole_haslo(driver_instance, input_text2)
    nacisnij_enter_naprzycisk_logowania(driver_instance)


def sprawdz_czy_gorne_logo_pasek_jest_widoczne(driver_instance):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__gorne_logo_pasek_xpath
    )
    return elem.is_displayed()


def sprawdz_czy_sekcja_logowania_jest_widoczna(driver_instance):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__sekcja_logowania_xpath
    )
    return elem.is_displayed()


def wprowadz_email_do_pole_email(driver_instance, text):
    wyslij_klucz_do_elementu(
        driver_instance=driver_instance,
        xpath=__pole_email_xpath,
        text=text
    )


def wprowadz_haslo_do_pole_haslo(driver_instance, text):
    wyslij_klucz_do_elementu(
        driver_instance=driver_instance,
        xpath=__pole_haslo_xpath,
        text=text
    )


def nacisnij_enter_naprzycisk_logowania(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__przycisk_logowania_xpath
    )


def nacisnij_enter_na_wyloguj_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__wyloguj_przycisk
    )


def sprawdz_czy_przycisk_wyloguj_jest_widoczny(driver_instance):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__wyloguj_przycisk
    )
    return elem.is_displayed()
