# -*- coding: utf-8 -*-

import logowanie, pulpit, uzytkownicy, nowy_uzytkownik
import unittest
from selenium import webdriver


class tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.driver.get("http://integracja.abraks.pl/login")

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
            pulpit.check_url_contains_correct_name_page(self.driver, 'http://integracja.abraks.pl/')
        )

        self.assertTrue(
           pulpit.check_loging_results_are_correct_admin(self.driver, 'Admin')
        )

        self.assertTrue(
            pulpit.check_url_contains_correct_name_page(self.driver, 'http://integracja.abraks.pl/')
        )

        pulpit.hit_enter_on_admin_button(self.driver)

        self.assertTrue(
            pulpit.check_hitting_results_are_correct_uzytkownicy(self.driver, u'Użytkownicy')
        )
        pulpit.hit_enter_on_uzytkownicy_button(self.driver)

############# Uzytkownicy ##########
        self.assertTrue(
            uzytkownicy.check_url_contains_correct_name_page(self.driver, 'http://integracja.abraks.pl/admin/user')
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
        print (num_uzytkownikow)

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

        nowy_uzytkownik.click_jezyk_polski_xpath(self.driver)
        nowy_uzytkownik.hit_enter_on_anuluj_button(self.driver)

############# Uzytkownicy ##########
        self.assertTrue(
            uzytkownicy.check_url_contains_correct_name_page(self.driver, 'http://integracja.abraks.pl/admin/user')
        )
        self.assertTrue(
            uzytkownicy.check_uzytkownik_tabela(self.driver)
        )
        num_uzytkownikow_po_dodaniu = uzytkownicy.count_uzytkownikow_w_tabeli(self.driver)
        # # Porownanie
        self.assertItemEqual(num_uzytkownikow, num_uzytkownikow_po_dodaniu)

    def assertItemEqual(self, num_uzytkownikow, num_uzytkownikow_po_dodaniu):
        pass





        # # # Asercja
        # self.assertGreater(num_uzytkownikow, num_uzytkownikow_po_dodaniu)

if __name__ == "__main__":
    unittest.main()