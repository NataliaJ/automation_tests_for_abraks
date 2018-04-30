# -*- coding: utf-8 -*-

import random
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

    def tearDown(self):
        self.driver.quit()

    def test_R_Test_4(self):
        input_text = "tester@abraks.pl"
        input_text2 = "Rety$675"

        self.assertTrue(logowanie.check_top_logo_bar_is_visible(self.driver))
        logowanie.input_email_to_email_field(self.driver, input_text)
        logowanie.input_password_to_password_field(self.driver, input_text2)
        logowanie.hit_enter_on_logging_button(self.driver)

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
        user_number = str(random.randint(0, 10000000))
        user_name = 'test' + user_number
        user_name_last_name = user_name + ' ' + user_name
        user_email = user_name + '@o2.pl'
        user_telefon_number = '123456789'
        self.assertTrue(
            nowy_uzytkownik.check_logo_utworz_uzytkownik(self.driver, u'Użytkownik > Utwórz')
        )
        self.assertTrue(
            nowy_uzytkownik.check_dodaj_uzytkownik_button(self.driver)
        )
        self.assertTrue(
            nowy_uzytkownik.check_anuluj_button(self.driver)
        )
        nowy_uzytkownik.input_text_to_nazwa_uzytkownika_xpath(self.driver, user_name)
        nowy_uzytkownik.input_text_to_email_xpath(self.driver, user_email)
        nowy_uzytkownik.input_text_to_imie_i_nazwisko_xpath(self.driver, user_name_last_name)
        nowy_uzytkownik.input_text_to_telefon_xpath(self.driver, user_telefon_number)
        nowy_uzytkownik.click_jezyk_polski_xpath(self.driver)
        nowy_uzytkownik.click_aktywny_tak_xpath(self.driver)
        nowy_uzytkownik.click_regulamin_zaakceptowany_tak_xpath(self.driver)
        nowy_uzytkownik.click_typ_uzytkownika_wewnetrzny(self.driver)
        nowy_uzytkownik.hit_enter_on_dodaj_uzytkownik_button(self.driver)

        ############# Uzytkownicy ##########
        self.assertTrue(
            uzytkownicy.check_url_contains_correct_name_page(self.driver, 'http://env20180415.abraks.pl/admin/user')
        )
        self.assertTrue(
            uzytkownicy.check_uzytkownik_tabela(self.driver)
        )
        num_uzytkownikow_po_dodaniu = uzytkownicy.count_uzytkownikow_w_tabeli(self.driver)

        # # # Asercja
        self.assertGreater(num_uzytkownikow_po_dodaniu, num_uzytkownikow)

    def test_R_Test_5(self):
        input_text = "tester@abraks.pl"
        input_text2 = "Rety$675"

        self.assertTrue(logowanie.check_top_logo_bar_is_visible(self.driver))
        logowanie.input_email_to_email_field(self.driver, input_text)
        logowanie.input_password_to_password_field(self.driver, input_text2)
        logowanie.hit_enter_on_logging_button(self.driver)

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
        user_number = str(random.randint(0, 10000000))
        user_name = 'test' + user_number
        user_name_last_name = user_name + ' ' + user_name
        user_email = user_name + '@o2.pl'
        user_telefon_number = '123456789'
        self.assertTrue(
            nowy_uzytkownik.check_logo_utworz_uzytkownik(self.driver, u'Użytkownik > Utwórz')
        )
        self.assertTrue(
            nowy_uzytkownik.check_dodaj_uzytkownik_button(self.driver)
        )
        self.assertTrue(
            nowy_uzytkownik.check_anuluj_button(self.driver)
        )
        nowy_uzytkownik.input_text_to_nazwa_uzytkownika_xpath(self.driver, user_name)
        nowy_uzytkownik.input_text_to_email_xpath(self.driver, user_email)
        nowy_uzytkownik.input_text_to_imie_i_nazwisko_xpath(self.driver, user_name_last_name)
        nowy_uzytkownik.input_text_to_telefon_xpath(self.driver, user_telefon_number)
        nowy_uzytkownik.click_jezyk_angielski_xpath(self.driver)
        nowy_uzytkownik.click_aktywny_tak_xpath(self.driver)
        nowy_uzytkownik.click_regulamin_zaakceptowany_tak_xpath(self.driver)
        nowy_uzytkownik.click_typ_uzytkownika_zewnetrzny(self.driver)
        nowy_uzytkownik.hit_enter_on_dodaj_uzytkownik_button(self.driver)

        ############# Uzytkownicy ##########
        self.assertTrue(
            uzytkownicy.check_url_contains_correct_name_page(self.driver, 'http://env20180415.abraks.pl/admin/user')
        )
        self.assertTrue(
            uzytkownicy.check_uzytkownik_tabela(self.driver)
        )
        num_uzytkownikow_po_dodaniu = uzytkownicy.count_uzytkownikow_w_tabeli(self.driver)

        # # # Asercja
        self.assertGreater(num_uzytkownikow_po_dodaniu, num_uzytkownikow)

    def test_R_Test_6(self):
        input_text = "tester@abraks.pl"
        input_text2 = "Rety$675"

        self.assertTrue(logowanie.check_top_logo_bar_is_visible(self.driver))
        logowanie.input_email_to_email_field(self.driver, input_text)
        logowanie.input_password_to_password_field(self.driver, input_text2)
        logowanie.hit_enter_on_logging_button(self.driver)

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
        user_number = str(random.randint(0, 10000000))
        user_name = 'test' + user_number
        user_name_last_name = user_name + ' ' + user_name
        user_email = user_name + '@o2.pl'
        user_telefon_number = '123456789'
        self.assertTrue(
            nowy_uzytkownik.check_logo_utworz_uzytkownik(self.driver, u'Użytkownik > Utwórz')
        )
        self.assertTrue(
            nowy_uzytkownik.check_dodaj_uzytkownik_button(self.driver)
        )
        self.assertTrue(
            nowy_uzytkownik.check_anuluj_button(self.driver)
        )
        nowy_uzytkownik.input_text_to_nazwa_uzytkownika_xpath(self.driver, user_name)
        nowy_uzytkownik.input_text_to_email_xpath(self.driver, user_email)
        nowy_uzytkownik.input_text_to_imie_i_nazwisko_xpath(self.driver, user_name_last_name)
        nowy_uzytkownik.input_text_to_telefon_xpath(self.driver, user_telefon_number)
        nowy_uzytkownik.click_jezyk_polski_xpath(self.driver)
        nowy_uzytkownik.click_aktywny_nie_xpath(self.driver)
        nowy_uzytkownik.click_regulamin_zaakceptowany_tak_xpath(self.driver)
        nowy_uzytkownik.click_typ_uzytkownika_wspolpracownik(self.driver)
        nowy_uzytkownik.hit_enter_on_dodaj_uzytkownik_button(self.driver)

        ############# Uzytkownicy ##########
        self.assertTrue(
            uzytkownicy.check_url_contains_correct_name_page(self.driver, 'http://env20180415.abraks.pl/admin/user')
        )
        self.assertTrue(
            uzytkownicy.check_uzytkownik_tabela(self.driver)
        )
        num_uzytkownikow_po_dodaniu = uzytkownicy.count_uzytkownikow_w_tabeli(self.driver)

        # # # Asercja
        self.assertGreater(num_uzytkownikow_po_dodaniu, num_uzytkownikow)

    def test_R_Test_7(self):
        input_text = "tester@abraks.pl"
        input_text2 = "Rety$675"

        self.assertTrue(logowanie.check_top_logo_bar_is_visible(self.driver))
        logowanie.input_email_to_email_field(self.driver, input_text)
        logowanie.input_password_to_password_field(self.driver, input_text2)
        logowanie.hit_enter_on_logging_button(self.driver)

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
        user_number = str(random.randint(0, 10000000))
        user_name = 'test' + user_number
        user_name_last_name = user_name + ' ' + user_name
        user_email = user_name + '@o2.pl'
        user_telefon_number = '123456789'
        self.assertTrue(
            nowy_uzytkownik.check_logo_utworz_uzytkownik(self.driver, u'Użytkownik > Utwórz')
        )
        self.assertTrue(
            nowy_uzytkownik.check_dodaj_uzytkownik_button(self.driver)
        )
        self.assertTrue(
            nowy_uzytkownik.check_anuluj_button(self.driver)
        )
        nowy_uzytkownik.input_text_to_nazwa_uzytkownika_xpath(self.driver, user_name)
        nowy_uzytkownik.input_text_to_email_xpath(self.driver, user_email)
        nowy_uzytkownik.input_text_to_imie_i_nazwisko_xpath(self.driver, user_name_last_name)
        nowy_uzytkownik.input_text_to_telefon_xpath(self.driver, user_telefon_number)
        nowy_uzytkownik.click_jezyk_polski_xpath(self.driver)
        nowy_uzytkownik.click_aktywny_tak_xpath(self.driver)
        nowy_uzytkownik.click_regulamin_zaakceptowany_nie_xpath(self.driver)
        nowy_uzytkownik.click_typ_uzytkownika_gosc(self.driver)
        nowy_uzytkownik.hit_enter_on_dodaj_uzytkownik_button(self.driver)

        ############# Uzytkownicy ##########
        self.assertTrue(
            uzytkownicy.check_url_contains_correct_name_page(self.driver, 'http://env20180415.abraks.pl/admin/user')
        )
        self.assertTrue(
            uzytkownicy.check_uzytkownik_tabela(self.driver)
        )
        num_uzytkownikow_po_dodaniu = uzytkownicy.count_uzytkownikow_w_tabeli(self.driver)

        # # # Asercja
        self.assertGreater(num_uzytkownikow_po_dodaniu, num_uzytkownikow)


if __name__ == "__main__":
    unittest.main()
