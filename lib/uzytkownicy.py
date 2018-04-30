# -*- coding: utf-8 -*-

from lib.funkcje_pomocnicze import *

# Xpaths

# Logo Uzytkownik
__uzytkownik_logo = "//*[@id='content']/div/div/h1"

# Tabela
__uzytkownik_tabela = "//*[@id='widget-grid']/div[2]/article/div[1]/table"

# Szukaj
__szukaj_xpath = "//*[@id='search_box']"

# Per strona
__per_strona = "//*[@id='perpage']/option[1]"

# Dodaj przycisk
__dodaj_przycisk = "//*[@id='dt_basic_filter']/a"

# Jezyk filtr
__jezyk_filtr = "//*[@id='language']"

# Aktywny filtr
__aktywny_filtr = "//*[@id='active']"

# Regulamin zaakceptowany filtr
__regulamin_zaakceptowany_filtr = "//*[@id='terms']"

# Typ Uzytkuwnika
__typ_uzytkownika_filtr = "//*[@id='type']"

# Lista Uzytkownikow
__lista_uzytkownikow = "//*[@id='widget-grid']/div[2]/article/div[1]/table/tbody[1]/tr"


def sprawdz_uzytkownik_logo(driver_instance, text):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__uzytkownik_logo
    )
    elem_text = elem.text
    return elem_text == text


def sprawdz_uzytkownik_tabela(driver_instance):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__uzytkownik_tabela
    )
    return elem


def sprawdz_uzytkownik_szukaj(driver_instance):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__szukaj_xpath
    )
    return elem


def sprawdz_uzytkownik_per_strona(driver_instance):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__per_strona
    )
    return elem


def sprawdz_uzytkownik_dodaj_przycisk(driver_instance):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__dodaj_przycisk
    )
    return elem


def sprawdz_uzytkownik_jezyk_filtr(driver_instance):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__jezyk_filtr
    )
    return elem


def sprawdz_uzytkownik_aktywny_filtr(driver_instance):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__aktywny_filtr
    )
    return elem


def sprawdz_uzytkownik_regulamin_zaakceptowany_filtr(driver_instance):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__regulamin_zaakceptowany_filtr
    )
    return elem


def sprawdz_uzytkownik_typ_uzytkownika_filtr(driver_instance):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=__typ_uzytkownika_filtr
    )
    return elem


def policz_uzytkownikow_w_tabeli(driver_instance):
    elems = poczekaj_na_widocznosc_wszystkich_elementow(
        driver_instance=driver_instance,
        xpath=__lista_uzytkownikow
    )
    return len(elems)


def nacisnij_enter_na_dodaj_przycisk(driver_instance):
    nacisnij_enter_na_elemencie(
        driver_instance=driver_instance,
        xpath=__dodaj_przycisk
    )
