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

##################### Klienci #############
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
        sekretariat.hit_enter_on_sekretariat_button(self.driver)
        self.assertTrue(
            sekretariat.check_hitting_results_are_correct_dokumenty(self.driver, 'Dokumenty')
        )
        sekretariat.hit_enter_on_sekretariat_dokumenty_button(self.driver)

########################## Sekretariat ###############

############## Dokumenty ###############
        self.assertTrue(
            sekretariat.check_url_contains_correct_name_page(self.driver, 'http://integracja.abraks.pl/secretariat/document')
        )
        self.assertTrue(
            sekretariat.check_sekretariat_logo(self.driver, u'Dokument > Indeks')
        )
        self.assertTrue(
            sekretariat.check_sekretariat_tabela(self.driver)
        )
        sekretariat.hit_enter_on_sekretariat_sprawy_button(self.driver)

############## Sprawy ###############
        self.assertTrue(
            sekretariat.check_url_contains_correct_name_page(self.driver, 'http://integracja.abraks.pl/secretariat/inquiry')
        )
        self.assertTrue(
            sekretariat.check_sekretariat_logo(self.driver, u'Sprawa > Indeks')
        )
        self.assertTrue(
            sekretariat.check_sekretariat_tabela(self.driver)
        )
        sekretariat.hit_enter_on_sekretariat_tematy_button(self.driver)

############## Tematy ###############
        self.assertTrue(
            sekretariat.check_url_contains_correct_name_page(self.driver, 'http://integracja.abraks.pl/secretariat/theme')
        )
        self.assertTrue(
            sekretariat.check_sekretariat_logo(self.driver, u'Temat > Indeks')
        )
        self.assertTrue(
            sekretariat.check_sekretariat_tabela(self.driver)
        )
        sekretariat.hit_enter_on_sekretariat_ksiazki_listow_button(self.driver)

############## Ksiazki Listowe ###############
        self.assertTrue(
            sekretariat.check_url_contains_correct_name_page(self.driver, 'href="http://integracja.abraks.pl/secretariat/summary"')
        )
        self.assertTrue(
            sekretariat.check_sekretariat_logo(self.driver, u'Książka Listowa > Indeks')
        )
        self.assertTrue(
            sekretariat.check_sekretariat_tabela(self.driver)
        )
        sekretariat.hit_enter_on_sekretariat_pisma_przychodzace_button(self.driver)

############## Pisma Przychodzace ###############
        self.assertTrue(
            sekretariat.check_url_contains_correct_name_page(self.driver, 'http://integracja.abraks.pl/secretariat/inbound')
        )
        self.assertTrue(
            sekretariat.check_sekretariat_logo(self.driver, u'Pismo Przychodzące > Indeks')
        )
        self.assertTrue(
            sekretariat.check_sekretariat_tabela(self.driver)
        )
        sekretariat.hit_enter_on_sekretariat_pisma_wychodzace_button(self.driver)

############## Pisma Wychodzace ###############
        self.assertTrue(
            sekretariat.check_url_contains_correct_name_page(self.driver, 'http://integracja.abraks.pl/secretariat/outbound')
        )
        self.assertTrue(
            sekretariat.check_sekretariat_logo(self.driver, u'Pismo Wychodzące > Indeks')
        )
        self.assertTrue(
            sekretariat.check_sekretariat_tabela(self.driver)
        )
        sekretariat.hit_enter_on_sekretariat_urlopy_button(self.driver)

############## Urlopy ###############
        self.assertTrue(
            sekretariat.check_url_contains_correct_name_page(self.driver, 'http://integracja.abraks.pl/secretariat/vacation')
        )
        self.assertTrue(
            sekretariat.check_sekretariat_logo(self.driver, u'Urlop > Indeks')
        )
        self.assertTrue(
            sekretariat.check_sekretariat_tabela(self.driver)
        )
        sekretariat.hit_enter_on_sekretariat_zadania_button(self.driver)

############## Zadania ###############
        self.assertTrue(
            sekretariat.check_url_contains_correct_name_page(self.driver, 'http://integracja.abraks.pl/secretariat/task')
        )
        self.assertTrue(
            sekretariat.check_sekretariat_logo(self.driver, u'Zadanie > Indeks')
        )
        self.assertTrue(
            sekretariat.check_sekretariat_tabela(self.driver)
        )
     #   klienci.hit_enter_on_ostrzezenia_button(self.driver)


if __name__ == "__main__":
    unittest.main()
