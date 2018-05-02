# -*- coding: utf-8 -*-

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

    def test_R_Test_1(self):

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
            uzytkownicy.sprawdz_uzytkownik_szukaj(self.driver)
        )
        self.assertTrue(
            uzytkownicy.sprawdz_uzytkownik_per_strona(self.driver)
        )
        self.assertTrue(
            uzytkownicy.sprawdz_uzytkownik_dodaj_przycisk(self.driver)
        )
        self.assertTrue(
            uzytkownicy.sprawdz_uzytkownik_jezyk_filtr(self.driver)
        )
        self.assertTrue(
            uzytkownicy.sprawdz_uzytkownik_aktywny_filtr(self.driver)
        )
        self.assertTrue(
            uzytkownicy.sprawdz_uzytkownik_regulamin_zaakceptowany_filtr(self.driver)
        )
        self.assertTrue(
            uzytkownicy.sprawdz_uzytkownik_typ_uzytkownika_filtr(self.driver)
        )

    def test_R_Test_2(self):

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
        self.assertTrue(
            nowy_uzytkownik.sprawdz_logo_utworz_uzytkownik(self.driver, u'Użytkownik > Utwórz')
        )
        self.assertTrue(
            nowy_uzytkownik.sprawdz_anuluj_przycisk(self.driver)
        )
        nowy_uzytkownik.nacisnij_enter_na_anuluj_przycisk(self.driver)

        ############# Uzytkownicy ##########
        self.assertTrue(
            uzytkownicy.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/admin/user')
        )
        self.assertTrue(
            uzytkownicy.sprawdz_uzytkownik_tabela(self.driver)
        )
        num_uzytkownikow_po_dodaniu = uzytkownicy.policz_uzytkownikow_w_tabeli(self.driver)
        # # Porownanie
        self.assertItemEqual(num_uzytkownikow, num_uzytkownikow_po_dodaniu)

    def test_R_Test_3(self):

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
        self.assertTrue(
            nowy_uzytkownik.sprawdz_logo_utworz_uzytkownik(self.driver, u'Użytkownik > Utwórz')
        )
        self.assertTrue(
            nowy_uzytkownik.sprawdz_dodaj_uzytkownik_przycisk(self.driver)
        )
        self.assertTrue(
            nowy_uzytkownik.sprawdz_anuluj_przycisk(self.driver)
        )
        nowy_uzytkownik.nacisnij_enter_na_dodaj_uzytkownik_przycisk(self.driver)

        self.assertTrue(
            nowy_uzytkownik.sprawdz_to_pole_jest_wymagane(self.driver)
        )

        nowy_uzytkownik.nacisnij_enter_na_anuluj_przycisk(self.driver)

        ############# Uzytkownicy ##########
        self.assertTrue(
            uzytkownicy.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/admin/user')
        )
        self.assertTrue(
            uzytkownicy.sprawdz_uzytkownik_tabela(self.driver)
        )
        num_uzytkownikow_po_dodaniu = uzytkownicy.policz_uzytkownikow_w_tabeli(self.driver)
        # # Porownanie
        self.assertItemEqual(num_uzytkownikow, num_uzytkownikow_po_dodaniu)

    def assertItemEqual(self, num_uzytkownikow, num_uzytkownikow_po_dodaniu):
        pass


if __name__ == "__main__":
    unittest.main()
