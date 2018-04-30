# -*- coding: utf-8 -*-

import unittest

import lib.logowanie as logowanie
import lib.nowy_uzytkownik as nowy_uzytkownik
import lib.pulpit as pulpit
import lib.uzytkownicy as uzytkownicy
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
            pulpit.check_loging_results_are_correct(self.driver, 'Pulpit > Indeks')
        )

        self.assertTrue(
            pulpit.check_url_contains_correct_name_page(self.driver, 'http://env20180415.abraks.pl/')
        )

        self.assertTrue(
            pulpit.check_loging_results_are_correct_admin(self.driver, 'Admin')
        )

        self.assertTrue(
            pulpit.check_url_contains_correct_name_page(self.driver, 'http://env20180415.abraks.pl/')
        )

        pulpit.hit_enter_on_admin_button(self.driver)

        self.assertTrue(
            pulpit.check_hitting_results_are_correct_uzytkownicy(self.driver, u'Użytkownicy')
        )
        pulpit.hit_enter_on_uzytkownicy_button(self.driver)

        ############# Uzytkownicy ##########
        self.assertTrue(
            uzytkownicy.check_url_contains_correct_name_page(self.driver, 'http://env20180415.abraks.pl/admin/user')
        )
        self.assertTrue(
            uzytkownicy.check_uzytkownik_logo(self.driver, u'Użytkownik > Indeks')
        )
        self.assertTrue(
            uzytkownicy.check_uzytkownik_tabela(self.driver)
        )
        self.assertTrue(
            uzytkownicy.check_uzytkownik_szukaj(self.driver)
        )
        self.assertTrue(
            uzytkownicy.check_uzytkownik_per_page(self.driver)
        )
        self.assertTrue(
            uzytkownicy.check_uzytkownik_dodaj_button(self.driver)
        )
        self.assertTrue(
            uzytkownicy.check_uzytkownik_jezyk_filtr(self.driver)
        )
        self.assertTrue(
            uzytkownicy.check_uzytkownik_aktywny_filtr(self.driver)
        )
        self.assertTrue(
            uzytkownicy.check_uzytkownik_regulamin_zaakceptowany_filtr(self.driver)
        )
        self.assertTrue(
            uzytkownicy.check_uzytkownik_typ_uzytkownika_filtr(self.driver)
        )

    def test_R_Test_2(self):

        self.assertTrue(
            pulpit.check_loging_results_are_correct(self.driver, 'Pulpit > Indeks')
        )

        self.assertTrue(
            pulpit.check_url_contains_correct_name_page(self.driver, 'http://env20180415.abraks.pl/')
        )

        self.assertTrue(
            pulpit.check_loging_results_are_correct_admin(self.driver, 'Admin')
        )

        self.assertTrue(
            pulpit.check_url_contains_correct_name_page(self.driver, 'http://env20180415.abraks.pl/')
        )

        pulpit.hit_enter_on_admin_button(self.driver)

        self.assertTrue(
            pulpit.check_hitting_results_are_correct_uzytkownicy(self.driver, u'Użytkownicy')
        )
        pulpit.hit_enter_on_uzytkownicy_button(self.driver)

        ############# Uzytkownicy ##########
        self.assertTrue(
            uzytkownicy.check_url_contains_correct_name_page(self.driver, 'http://env20180415.abraks.pl/admin/user')
        )
        self.assertTrue(
            uzytkownicy.check_uzytkownik_logo(self.driver, u'Użytkownik > Indeks')
        )
        self.assertTrue(
            uzytkownicy.check_uzytkownik_tabela(self.driver)
        )
        self.assertTrue(
            uzytkownicy.check_uzytkownik_dodaj_button(self.driver)
        )
        num_uzytkownikow = uzytkownicy.count_uzytkownikow_w_tabeli(self.driver)

        uzytkownicy.hit_enter_on_dodaj_button(self.driver)

        ############# Nowy Uzytkownik ######################
        self.assertTrue(
            nowy_uzytkownik.check_logo_utworz_uzytkownik(self.driver, u'Użytkownik > Utwórz')
        )
        self.assertTrue(
            nowy_uzytkownik.check_anuluj_button(self.driver)
        )
        nowy_uzytkownik.hit_enter_on_anuluj_button(self.driver)

        ############# Uzytkownicy ##########
        self.assertTrue(
            uzytkownicy.check_url_contains_correct_name_page(self.driver, 'http://env20180415.abraks.pl/admin/user')
        )
        self.assertTrue(
            uzytkownicy.check_uzytkownik_tabela(self.driver)
        )
        num_uzytkownikow_po_dodaniu = uzytkownicy.count_uzytkownikow_w_tabeli(self.driver)
        # # Porownanie
        self.assertItemEqual(num_uzytkownikow, num_uzytkownikow_po_dodaniu)

    def test_R_Test_3(self):
        self.assertTrue(
            pulpit.check_loging_results_are_correct(self.driver, 'Pulpit > Indeks')
        )

        self.assertTrue(
            pulpit.check_url_contains_correct_name_page(self.driver, 'http://env20180415.abraks.pl/')
        )

        self.assertTrue(
            pulpit.check_loging_results_are_correct_admin(self.driver, 'Admin')
        )

        self.assertTrue(
            pulpit.check_url_contains_correct_name_page(self.driver, 'http://env20180415.abraks.pl/')
        )

        pulpit.hit_enter_on_admin_button(self.driver)

        self.assertTrue(
            pulpit.check_hitting_results_are_correct_uzytkownicy(self.driver, u'Użytkownicy')
        )
        pulpit.hit_enter_on_uzytkownicy_button(self.driver)

        ############# Uzytkownicy ##########
        self.assertTrue(
            uzytkownicy.check_url_contains_correct_name_page(self.driver, 'http://env20180415.abraks.pl/admin/user')
        )
        self.assertTrue(
            uzytkownicy.check_uzytkownik_logo(self.driver, u'Użytkownik > Indeks')
        )
        self.assertTrue(
            uzytkownicy.check_uzytkownik_tabela(self.driver)
        )
        self.assertTrue(
            uzytkownicy.check_uzytkownik_dodaj_button(self.driver)
        )
        num_uzytkownikow = uzytkownicy.count_uzytkownikow_w_tabeli(self.driver)

        uzytkownicy.hit_enter_on_dodaj_button(self.driver)

        ############# Nowy Uzytkownik ######################
        self.assertTrue(
            nowy_uzytkownik.check_logo_utworz_uzytkownik(self.driver, u'Użytkownik > Utwórz')
        )
        self.assertTrue(
            nowy_uzytkownik.check_dodaj_uzytkownik_button(self.driver)
        )
        self.assertTrue(
            nowy_uzytkownik.check_anuluj_button(self.driver)
        )
        nowy_uzytkownik.hit_enter_on_dodaj_uzytkownik_button(self.driver)

        self.assertTrue(
            nowy_uzytkownik.check_to_pole_jest_wymagane(self.driver)
        )

        nowy_uzytkownik.hit_enter_on_anuluj_button(self.driver)

        ############# Uzytkownicy ##########
        self.assertTrue(
            uzytkownicy.check_url_contains_correct_name_page(self.driver, 'http://env20180415.abraks.pl/admin/user')
        )
        self.assertTrue(
            uzytkownicy.check_uzytkownik_tabela(self.driver)
        )
        num_uzytkownikow_po_dodaniu = uzytkownicy.count_uzytkownikow_w_tabeli(self.driver)
        # # Porownanie
        self.assertItemEqual(num_uzytkownikow, num_uzytkownikow_po_dodaniu)

    def assertItemEqual(self, num_uzytkownikow, num_uzytkownikow_po_dodaniu):
        pass


if __name__ == "__main__":
    unittest.main()
