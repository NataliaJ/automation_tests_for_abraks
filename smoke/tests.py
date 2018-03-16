# -*- coding: utf-8 -*-

import logowanie, pulpit, klienci, sekretariat, admin
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

    def test_loging_correct_results(self):
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
           pulpit.check_loging_results_are_correct_klinci(self.driver, 'Klienci')
        )

        self.assertTrue(
            pulpit.check_url_contains_correct_name_page(self.driver, 'http://integracja.abraks.pl/')
        )

        pulpit.hit_enter_on_klienci_button(self.driver)

        self.assertTrue(
            pulpit.check_hitting_results_are_correct_kontrahenci(self.driver, 'Kontrahenci')
        )
        pulpit.hit_enter_on_kontrahenci_button(self.driver)
############# Kontrahenci #############
        self.assertTrue(
            klienci.check_url_contains_correct_name_page(self.driver, 'http://integracja.abraks.pl/customer/contractor')
        )
        self.assertTrue(
            klienci.check_klienci_logo(self.driver, 'Kontrahent > Indeks')
        )
        self.assertTrue(
            klienci.check_klienci_tabela(self.driver)
        )
        klienci.hit_enter_on_oddzialy_button(self.driver)
############## Oddzialy ###############
        self.assertTrue(
            klienci.check_url_contains_correct_name_page(self.driver, 'http://integracja.abraks.pl/customer/department')
        )
        self.assertTrue(
            klienci.check_klienci_logo(self.driver, u'Oddział > Indeks')
        )
        self.assertTrue(
            klienci.check_klienci_tabela(self.driver)
        )
        klienci.hit_enter_on_osoby_kontaktowe_button(self.driver)

############## Osoby kontaktowe ###############

        self.assertTrue(
            klienci.check_url_contains_correct_name_page(self.driver, 'http://integracja.abraks.pl/customer/person')
        )
        self.assertTrue(
            klienci.check_klienci_logo(self.driver, 'Osoba Kontaktowa > Indeks')
        )
        self.assertTrue(
            klienci.check_klienci_tabela(self.driver)
        )
        klienci.hit_enter_on_ostrzezenia_button(self.driver)

############## Ostrzezenia ###############
        self.assertTrue(
            klienci.check_url_contains_correct_name_page(self.driver, 'http://integracja.abraks.pl/customer/warning')
        )
        self.assertTrue(
            klienci.check_klienci_logo(self.driver, u'Ostrzeżenie > Indeks')
        )
        self.assertTrue(
            klienci.check_klienci_tabela(self.driver)
        )
     #   klienci.hit_enter_on_ostrzezenia_button(self.driver)


if __name__ == "__main__":
    unittest.main()
