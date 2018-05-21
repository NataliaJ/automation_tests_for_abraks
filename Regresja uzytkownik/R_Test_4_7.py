# -*- coding: utf-8 -*-

import random
import unittest

import Funkcje.logowanie as logowanie
import Funkcje.nowy_uzytkownik as nowy_uzytkownik
import Funkcje.pulpit as pulpit
import Funkcje.uzytkownicy as uzytkownicy
from selenium import webdriver


class tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.driver.get("http://env20180415.abraks.pl/login")
        logowanie.login(self, self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_R_Test_4(self):

        self.assertTrue(
            pulpit.sprawdz_poprawnosc_logowania(self.driver, 'Pulpit > Indeks')
        )

        self.assertTrue(
            pulpit.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/')
        )

        self.assertTrue(
            pulpit.sprawdz_poprawnosc_logowania_admin(self.driver, 'Admin')
        )

        self.assertTrue(
            pulpit.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/')
        )

        pulpit.nacisnij_enter_na_admin_przycisk(self.driver)

        self.assertTrue(
            pulpit.sprawdz_poprawnosc_nacisniecia_uzytkownicy(self.driver, u'Użytkownicy')
        )
        pulpit.nacisnij_enter_na_uzytkownicy_przycisk(self.driver)

        ############# Uzytkownicy ##########
        self.assertTrue(
            uzytkownicy.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/admin/user')
        )
        self.assertTrue(
            uzytkownicy.sprawdz_uzytkownik_logo(self.driver, u'Użytkownik > Indeks')
        )
        self.assertTrue(
            uzytkownicy.sprawdz_uzytkownik_tabela(self.driver)
        )
        self.assertTrue(
            uzytkownicy.sprawdz_uzytkownik_dodaj_przycisk(self.driver)
        )
        num_uzytkownikow = uzytkownicy.policz_uzytkownikow_w_tabeli(self.driver)

        uzytkownicy.nacisnij_enter_na_dodaj_przycisk(self.driver)

        ############# Nowy Uzytkownik ######################
        numer_uzytkownika = str(random.randint(0, 10000000))
        imie_uzytkownika = 'test' + numer_uzytkownika
        imie_i_nazwisko_uzytkownika = imie_uzytkownika + ' ' + imie_uzytkownika
        email_uzytkownika = imie_uzytkownika + '@o2.pl'
        telefon_uzytkownika = '123456789'
        self.assertTrue(
            nowy_uzytkownik.sprawdz_logo_utworz_uzytkownik(self.driver, u'Użytkownik > Utwórz')
        )
        self.assertTrue(
            nowy_uzytkownik.sprawdz_dodaj_uzytkownik_przycisk(self.driver)
        )
        self.assertTrue(
            nowy_uzytkownik.sprawdz_anuluj_przycisk(self.driver)
        )
        nowy_uzytkownik.wprowadz_text_do_nazwa_uzytkownika_xpath(self.driver, imie_uzytkownika)
        nowy_uzytkownik.wprowadz_text_do_email_xpath(self.driver, email_uzytkownika)
        nowy_uzytkownik.wprowadz_text_do_imie_i_nazwisko_xpath(self.driver, imie_i_nazwisko_uzytkownika)
        nowy_uzytkownik.wprowadz_text_do_telefon_xpath(self.driver, telefon_uzytkownika)
        nowy_uzytkownik.kliknij_jezyk_polski_xpath(self.driver)
        nowy_uzytkownik.kliknij_aktywny_tak_xpath(self.driver)
        nowy_uzytkownik.kliknij_regulamin_zaakceptowany_tak_xpath(self.driver)
        nowy_uzytkownik.kliknij_typ_uzytkownika_wewnetrzny(self.driver)
        nowy_uzytkownik.nacisnij_enter_na_dodaj_uzytkownik_przycisk(self.driver)

        ############# Uzytkownicy ##########
        self.assertTrue(
            uzytkownicy.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/admin/user')
        )
        self.assertTrue(
            uzytkownicy.sprawdz_uzytkownik_tabela(self.driver)
        )
        num_uzytkownikow_po_dodaniu = uzytkownicy.policz_uzytkownikow_w_tabeli(self.driver)

        # # # Asercja
        self.assertGreater(num_uzytkownikow_po_dodaniu, num_uzytkownikow)

    def test_R_Test_5(self):

        self.assertTrue(
            pulpit.sprawdz_poprawnosc_logowania(self.driver, 'Pulpit > Indeks')
        )

        self.assertTrue(
            pulpit.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/')
        )

        self.assertTrue(
            pulpit.sprawdz_poprawnosc_logowania_admin(self.driver, 'Admin')
        )

        self.assertTrue(
            pulpit.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/')
        )

        pulpit.nacisnij_enter_na_admin_przycisk(self.driver)

        self.assertTrue(
            pulpit.sprawdz_poprawnosc_nacisniecia_uzytkownicy(self.driver, u'Użytkownicy')
        )
        pulpit.nacisnij_enter_na_uzytkownicy_przycisk(self.driver)

        ############# Uzytkownicy ##########
        self.assertTrue(
            uzytkownicy.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/admin/user')
        )
        self.assertTrue(
            uzytkownicy.sprawdz_uzytkownik_logo(self.driver, u'Użytkownik > Indeks')
        )
        self.assertTrue(
            uzytkownicy.sprawdz_uzytkownik_tabela(self.driver)
        )
        self.assertTrue(
            uzytkownicy.sprawdz_uzytkownik_dodaj_przycisk(self.driver)
        )
        num_uzytkownikow = uzytkownicy.policz_uzytkownikow_w_tabeli(self.driver)

        uzytkownicy.nacisnij_enter_na_dodaj_przycisk(self.driver)

        ############# Nowy Uzytkownik ######################
        numer_uzytkownika = str(random.randint(0, 10000000))
        imie_uzytkownika = 'test' + numer_uzytkownika
        imie_i_nazwisko_uzytkownika = imie_uzytkownika + ' ' + imie_uzytkownika
        email_uzytkownika = imie_uzytkownika + '@o2.pl'
        telefon_uzytkownika = '123456789'
        self.assertTrue(
            nowy_uzytkownik.sprawdz_logo_utworz_uzytkownik(self.driver, u'Użytkownik > Utwórz')
        )
        self.assertTrue(
            nowy_uzytkownik.sprawdz_dodaj_uzytkownik_przycisk(self.driver)
        )
        self.assertTrue(
            nowy_uzytkownik.sprawdz_anuluj_przycisk(self.driver)
        )
        nowy_uzytkownik.wprowadz_text_do_nazwa_uzytkownika_xpath(self.driver, imie_uzytkownika)
        nowy_uzytkownik.wprowadz_text_do_email_xpath(self.driver, email_uzytkownika)
        nowy_uzytkownik.wprowadz_text_do_imie_i_nazwisko_xpath(self.driver, imie_i_nazwisko_uzytkownika)
        nowy_uzytkownik.wprowadz_text_do_telefon_xpath(self.driver, telefon_uzytkownika)
        nowy_uzytkownik.kliknij_jezyk_angielski_xpath(self.driver)
        nowy_uzytkownik.kliknij_aktywny_tak_xpath(self.driver)
        nowy_uzytkownik.kliknij_regulamin_zaakceptowany_tak_xpath(self.driver)
        nowy_uzytkownik.kliknij_typ_uzytkownika_zewnetrzny(self.driver)
        nowy_uzytkownik.nacisnij_enter_na_dodaj_uzytkownik_przycisk(self.driver)

        ############# Uzytkownicy ##########
        self.assertTrue(
            uzytkownicy.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/admin/user')
        )
        self.assertTrue(
            uzytkownicy.sprawdz_uzytkownik_tabela(self.driver)
        )
        num_uzytkownikow_po_dodaniu = uzytkownicy.policz_uzytkownikow_w_tabeli(self.driver)

        # # # Asercja
        self.assertGreater(num_uzytkownikow_po_dodaniu, num_uzytkownikow)

    def test_R_Test_6(self):

        self.assertTrue(
            pulpit.sprawdz_poprawnosc_logowania(self.driver, 'Pulpit > Indeks')
        )

        self.assertTrue(
            pulpit.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/')
        )

        self.assertTrue(
            pulpit.sprawdz_poprawnosc_logowania_admin(self.driver, 'Admin')
        )

        self.assertTrue(
            pulpit.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/')
        )

        pulpit.nacisnij_enter_na_admin_przycisk(self.driver)

        self.assertTrue(
            pulpit.sprawdz_poprawnosc_nacisniecia_uzytkownicy(self.driver, u'Użytkownicy')
        )
        pulpit.nacisnij_enter_na_uzytkownicy_przycisk(self.driver)

        ############# Uzytkownicy ##########
        self.assertTrue(
            uzytkownicy.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/admin/user')
        )
        self.assertTrue(
            uzytkownicy.sprawdz_uzytkownik_logo(self.driver, u'Użytkownik > Indeks')
        )
        self.assertTrue(
            uzytkownicy.sprawdz_uzytkownik_tabela(self.driver)
        )
        self.assertTrue(
            uzytkownicy.sprawdz_uzytkownik_dodaj_przycisk(self.driver)
        )
        num_uzytkownikow = uzytkownicy.policz_uzytkownikow_w_tabeli(self.driver)

        uzytkownicy.nacisnij_enter_na_dodaj_przycisk(self.driver)

        ############# Nowy Uzytkownik ######################
        numer_uzytkownika = str(random.randint(0, 10000000))
        imie_uzytkownika = 'test' + numer_uzytkownika
        imie_i_nazwisko_uzytkownika = imie_uzytkownika + ' ' + imie_uzytkownika
        email_uzytkownika = imie_uzytkownika + '@o2.pl'
        telefon_uzytkownika = '123456789'
        self.assertTrue(
            nowy_uzytkownik.sprawdz_logo_utworz_uzytkownik(self.driver, u'Użytkownik > Utwórz')
        )
        self.assertTrue(
            nowy_uzytkownik.sprawdz_dodaj_uzytkownik_przycisk(self.driver)
        )
        self.assertTrue(
            nowy_uzytkownik.sprawdz_anuluj_przycisk(self.driver)
        )
        nowy_uzytkownik.wprowadz_text_do_nazwa_uzytkownika_xpath(self.driver, imie_uzytkownika)
        nowy_uzytkownik.wprowadz_text_do_email_xpath(self.driver, email_uzytkownika)
        nowy_uzytkownik.wprowadz_text_do_imie_i_nazwisko_xpath(self.driver, imie_i_nazwisko_uzytkownika)
        nowy_uzytkownik.wprowadz_text_do_telefon_xpath(self.driver, telefon_uzytkownika)
        nowy_uzytkownik.kliknij_jezyk_polski_xpath(self.driver)
        nowy_uzytkownik.kliknij_aktywny_nie_xpath(self.driver)
        nowy_uzytkownik.kliknij_regulamin_zaakceptowany_tak_xpath(self.driver)
        nowy_uzytkownik.kliknij_typ_uzytkownika_wspolpracownik(self.driver)
        nowy_uzytkownik.nacisnij_enter_na_dodaj_uzytkownik_przycisk(self.driver)

        ############# Uzytkownicy ##########
        self.assertTrue(
            uzytkownicy.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/admin/user')
        )
        self.assertTrue(
            uzytkownicy.sprawdz_uzytkownik_tabela(self.driver)
        )
        num_uzytkownikow_po_dodaniu = uzytkownicy.policz_uzytkownikow_w_tabeli(self.driver)

        # # # Asercja
        self.assertGreater(num_uzytkownikow_po_dodaniu, num_uzytkownikow)

    def test_R_Test_7(self):

        self.assertTrue(
            pulpit.sprawdz_poprawnosc_logowania(self.driver, 'Pulpit > Indeks')
        )

        self.assertTrue(
            pulpit.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/')
        )

        self.assertTrue(
            pulpit.sprawdz_poprawnosc_logowania_admin(self.driver, 'Admin')
        )

        self.assertTrue(
            pulpit.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/')
        )

        pulpit.nacisnij_enter_na_admin_przycisk(self.driver)

        self.assertTrue(
            pulpit.sprawdz_poprawnosc_nacisniecia_uzytkownicy(self.driver, u'Użytkownicy')
        )
        pulpit.nacisnij_enter_na_uzytkownicy_przycisk(self.driver)

        ############# Uzytkownicy ##########
        self.assertTrue(
            uzytkownicy.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/admin/user')
        )
        self.assertTrue(
            uzytkownicy.sprawdz_uzytkownik_logo(self.driver, u'Użytkownik > Indeks')
        )
        self.assertTrue(
            uzytkownicy.sprawdz_uzytkownik_tabela(self.driver)
        )
        self.assertTrue(
            uzytkownicy.sprawdz_uzytkownik_dodaj_przycisk(self.driver)
        )
        num_uzytkownikow = uzytkownicy.policz_uzytkownikow_w_tabeli(self.driver)

        uzytkownicy.nacisnij_enter_na_dodaj_przycisk(self.driver)

        ############# Nowy Uzytkownik ######################
        numer_uzytkownika = str(random.randint(0, 10000000))
        imie_uzytkownika = 'test' + numer_uzytkownika
        imie_i_nazwisko_uzytkownika = imie_uzytkownika + ' ' + imie_uzytkownika
        email_uzytkownika = imie_uzytkownika + '@o2.pl'
        telefon_uzytkownika = '123456789'
        self.assertTrue(
            nowy_uzytkownik.sprawdz_logo_utworz_uzytkownik(self.driver, u'Użytkownik > Utwórz')
        )
        self.assertTrue(
            nowy_uzytkownik.sprawdz_dodaj_uzytkownik_przycisk(self.driver)
        )
        self.assertTrue(
            nowy_uzytkownik.sprawdz_anuluj_przycisk(self.driver)
        )
        nowy_uzytkownik.wprowadz_text_do_nazwa_uzytkownika_xpath(self.driver, imie_uzytkownika)
        nowy_uzytkownik.wprowadz_text_do_email_xpath(self.driver, email_uzytkownika)
        nowy_uzytkownik.wprowadz_text_do_imie_i_nazwisko_xpath(self.driver, imie_i_nazwisko_uzytkownika)
        nowy_uzytkownik.wprowadz_text_do_telefon_xpath(self.driver, telefon_uzytkownika)
        nowy_uzytkownik.kliknij_jezyk_polski_xpath(self.driver)
        nowy_uzytkownik.kliknij_aktywny_tak_xpath(self.driver)
        nowy_uzytkownik.kliknij_regulamin_zaakceptowany_nie_xpath(self.driver)
        nowy_uzytkownik.kliknij_typ_uzytkownika_gosc(self.driver)
        nowy_uzytkownik.nacisnij_enter_na_dodaj_uzytkownik_przycisk(self.driver)

        ############# Uzytkownicy ##########
        self.assertTrue(
            uzytkownicy.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/admin/user')
        )
        self.assertTrue(
            uzytkownicy.sprawdz_uzytkownik_tabela(self.driver)
        )
        num_uzytkownikow_po_dodaniu = uzytkownicy.policz_uzytkownikow_w_tabeli(self.driver)

        # # # Asercja
        self.assertGreater(num_uzytkownikow_po_dodaniu, num_uzytkownikow)


if __name__ == "__main__":
    unittest.main()
