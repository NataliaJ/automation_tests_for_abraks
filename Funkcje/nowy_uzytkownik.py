# -*- coding: utf-8 -*-

from Funkcje.funkcje_pomocnicze import *

# Xpaths

# Logo Uzytkownik utworz
__logo_utworz_uzytkownik = "//*[@id='content']/div/div/h1"

# Anuluj przycisk
__anuluj_przycisk = "//*[@id='admin_user_manage']/footer/a"

# Dodaj Uzytkownika przycisk
__dodaj_uzytkownika_przycisk = "//*[@id='admin_user_manage']/footer/button"

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


def sprawdz_logo_utworz_uzytkownik(driver_instance, text):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__logo_utworz_uzytkownik
    )
    elem_text = elem.text
    return elem_text == text


def sprawdz_anuluj_przycisk(driver_instance):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__anuluj_przycisk
    )
    return elem


def sprawdz_dodaj_uzytkownik_przycisk(driver_instance):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__dodaj_uzytkownika_przycisk
    )
    return elem


def sprawdz_to_pole_jest_wymagane(driver_instance):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__to_pole_jest_wymagane
    )
    return elem


def sprawdz_nazwa_uzytkownika_xpath(driver_instance):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__nazwa_uzytkownika_xpath
    )
    return elem


def nacisnij_enter_na_anuluj_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__anuluj_przycisk
    )


def nacisnij_enter_na_dodaj_uzytkownik_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__dodaj_uzytkownika_przycisk
    )


def wprowadz_text_do_nazwa_uzytkownika_xpath(driver_instance, text):
    wyslij_klucz_do_elementu(
        driver_instance=driver_instance,
        xpath=__nazwa_uzytkownika_xpath,
        text=text
    )


def wprowadz_text_do_email_xpath(driver_instance, text):
    wyslij_klucz_do_elementu(
        driver_instance=driver_instance,
        xpath=__email_xpath,
        text=text
    )


def wprowadz_text_do_imie_i_nazwisko_xpath(driver_instance, text):
    wyslij_klucz_do_elementu(
        driver_instance=driver_instance,
        xpath=__imie_i_nazwisko_xpath,
        text=text
    )


def wprowadz_text_do_telefon_xpath(driver_instance, text):
    wyslij_klucz_do_elementu(
        driver_instance=driver_instance,
        xpath=__telefon_xpath,
        text=text
    )


def kliknij_jezyk_polski_xpath(driver_instance):
    elem = poczekaj_na_obecnosc_elementu(
        driver_instance=driver_instance,
        xpath=__jezyk_polski_xpath
    )
    elem.click()


def kliknij_jezyk_angielski_xpath(driver_instance):
    elem = poczekaj_na_obecnosc_elementu(
        driver_instance=driver_instance,
        xpath=__jezyk_angielski_xpath
    )
    elem.click()


def kliknij_aktywny_tak_xpath(driver_instance):
    elem = poczekaj_na_obecnosc_elementu(
        driver_instance=driver_instance,
        xpath=__aktywny_tak_xpath
    )
    elem.click()


def kliknij_aktywny_nie_xpath(driver_instance):
    elem = poczekaj_na_obecnosc_elementu(
        driver_instance=driver_instance,
        xpath=__aktywny_nie_xpath
    )
    elem.click()


def kliknij_regulamin_zaakceptowany_tak_xpath(driver_instance):
    elem = poczekaj_na_obecnosc_elementu(
        driver_instance=driver_instance,
        xpath=__regulamin_zaakceptowany_tak_xpath
    )
    elem.click()


def kliknij_regulamin_zaakceptowany_nie_xpath(driver_instance):
    elem = poczekaj_na_obecnosc_elementu(
        driver_instance=driver_instance,
        xpath=__regulamin_zaakceptowany_nie_xpath
    )
    elem.click()


def kliknij_typ_uzytkownika_wewnetrzny(driver_instance):
    elem = poczekaj_na_obecnosc_elementu(
        driver_instance=driver_instance,
        xpath=__typ_uzytkownika_wewnetrzny
    )
    elem.click()


def kliknij_typ_uzytkownika_zewnetrzny(driver_instance):
    elem = poczekaj_na_obecnosc_elementu(
        driver_instance=driver_instance,
        xpath=__typ_uzytkownika_zewnetrzny
    )
    elem.click()


def kliknij_typ_uzytkownika_wspolpracownik(driver_instance):
    elem = poczekaj_na_obecnosc_elementu(
        driver_instance=driver_instance,
        xpath=__typ_uzytkownika_wspolpracownik
    )
    elem.click()


def kliknij_typ_uzytkownika_gosc(driver_instance):
    elem = poczekaj_na_obecnosc_elementu(
        driver_instance=driver_instance,
        xpath=__typ_uzytkownika_gosc
    )
    elem.click()
