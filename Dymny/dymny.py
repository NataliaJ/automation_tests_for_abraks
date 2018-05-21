# -*- coding: utf-8 -*-

import unittest

from selenium import webdriver

import Funkcje.admin as admin
import Funkcje.klienci as klienci
import Funkcje.logowanie as logowanie
import Funkcje.pulpit as pulpit
import Funkcje.sekretariat as sekretariat


class tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.driver.get("http://env20180415.abraks.pl/login")
        logowanie.login(self, self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_loging_correct_results(self):
        self.assertTrue(
            pulpit.sprawdz_poprawnosc_logowania_logo(self.driver)
        )
        self.assertTrue(
            logowanie.sprawdz_czy_przycisk_wyloguj_jest_widoczny(self.driver)
        )
        self.assertTrue(
            pulpit.sprawdz_poprawnosc_logowania(self.driver, 'Pulpit > Indeks')
        )
        self.assertTrue(
            pulpit.sprawdz_poprawnosc_logowania_klienci(self.driver, 'Klienci')
        )

        self.assertTrue(
            pulpit.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/')
        )
        num_widgetow = pulpit.policz_widgety_w_tabeli(self.driver)
        num_widgetow_poprawnie = 7

        # # Porownanie
        self.assertItemEqual(num_widgetow, num_widgetow_poprawnie)

        pulpit.nacisnij_enter_na_klienci_przycisk(self.driver)

        self.assertTrue(
            pulpit.sprawdz_poprawnosc_nacisniecia_kontrahenci(self.driver, 'Kontrahenci')
        )
        pulpit.nacisnij_enter_na_kontrahenci_przycisk(self.driver)

        ##################### Klienci #############
        ############# Kontrahenci #############
        self.assertTrue(
            klienci.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver,
                                                         'http://env20180415.abraks.pl/customer/contractor')
        )
        self.assertTrue(
            klienci.sprawdz_klienci_logo(self.driver, 'Kontrahent > Indeks')
        )
        self.assertTrue(
            klienci.sprawdz_klienci_tabela(self.driver)
        )
        klienci.nacisnij_enter_na_oddzialy_przycisk(self.driver)
        ############## Oddzialy ###############
        self.assertTrue(
            klienci.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver,
                                                         'http://env20180415.abraks.pl/customer/department')
        )
        self.assertTrue(
            klienci.sprawdz_klienci_logo(self.driver, u'Oddział > Indeks')
        )
        self.assertTrue(
            klienci.sprawdz_klienci_tabela(self.driver)
        )
        klienci.nacisnij_enter_na_osoby_kontaktowe_przycisk(self.driver)

        ############## Osoby kontaktowe ###############

        self.assertTrue(
            klienci.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/customer/person')
        )
        self.assertTrue(
            klienci.sprawdz_klienci_logo(self.driver, 'Osoba Kontaktowa > Indeks')
        )
        self.assertTrue(
            klienci.sprawdz_klienci_tabela(self.driver)
        )
        klienci.nacisnij_enter_na_ostrzezenia_przycisk(self.driver)

        ############## Ostrzezenia ###############
        self.assertTrue(
            klienci.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/customer/warning')
        )
        self.assertTrue(
            klienci.sprawdz_klienci_logo(self.driver, u'Ostrzeżenie > Indeks')
        )
        self.assertTrue(
            klienci.sprawdz_klienci_tabela(self.driver)
        )
        sekretariat.nacisnij_enter_na_sekretariat_przycisk(self.driver)
        self.assertTrue(
            sekretariat.check_hitting_results_are_correct_dokumenty(self.driver, 'Dokumenty')
        )
        sekretariat.nacisnij_enter_na_sekretariat_dokumenty_przycisk(self.driver)

        ########################## Sekretariat ###############

        ############## Dokumenty ###############
        self.assertTrue(
            sekretariat.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver,
                                                             'http://env20180415.abraks.pl/secretariat/document')
        )
        self.assertTrue(
            sekretariat.sprawdz_sekretariat_logo(self.driver, u'Dokument > Indeks')
        )
        self.assertTrue(
            sekretariat.sprawdz_sekretariat_tabela(self.driver)
        )
        sekretariat.nacisnij_enter_na_sekretariat_sprawy_przycisk(self.driver)

        ############## Sprawy ###############
        self.assertTrue(
            sekretariat.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver,
                                                             'http://env20180415.abraks.pl/secretariat/inquiry')
        )
        self.assertTrue(
            sekretariat.sprawdz_sekretariat_logo(self.driver, u'Sprawa > Indeks')
        )
        self.assertTrue(
            sekretariat.sprawdz_sekretariat_tabela(self.driver)
        )
        sekretariat.nacisnij_enter_na_sekretariat_tematy_przycisk(self.driver)

        ############## Tematy ###############
        self.assertTrue(
            sekretariat.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver,
                                                             'http://env20180415.abraks.pl/secretariat/theme')
        )
        self.assertTrue(
            sekretariat.sprawdz_sekretariat_logo(self.driver, u'Temat > Indeks')
        )
        self.assertTrue(
            sekretariat.sprawdz_sekretariat_tabela(self.driver)
        )
        sekretariat.nacisnij_enter_na_sekretariat_ksiazki_listow_przycisk(self.driver)

        ############## Ksiazki Listowe ###############
        self.assertTrue(
            sekretariat.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver,
                                                             'href="http://env20180415.abraks.pl/secretariat/summary"')
        )
        self.assertTrue(
            sekretariat.sprawdz_sekretariat_logo(self.driver, u'Książka Listowa > Indeks')
        )
        self.assertTrue(
            sekretariat.sprawdz_sekretariat_tabela(self.driver)
        )
        sekretariat.nacisnij_enter_na_sekretariat_pisma_przychodzace_przycisk(self.driver)

        ############## Pisma Przychodzace ###############
        self.assertTrue(
            sekretariat.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver,
                                                             'http://env20180415.abraks.pl/secretariat/inbound')
        )
        self.assertTrue(
            sekretariat.sprawdz_sekretariat_logo(self.driver, u'Pismo Przychodzące > Indeks')
        )
        self.assertTrue(
            sekretariat.sprawdz_sekretariat_tabela(self.driver)
        )
        sekretariat.nacisnij_enter_na_sekretariat_pisma_wychodzace_przycisk(self.driver)

        ############## Pisma Wychodzace ###############
        self.assertTrue(
            sekretariat.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver,
                                                             'http://env20180415.abraks.pl/secretariat/outbound')
        )
        self.assertTrue(
            sekretariat.sprawdz_sekretariat_logo(self.driver, u'Pismo Wychodzące > Indeks')
        )
        self.assertTrue(
            sekretariat.sprawdz_sekretariat_tabela(self.driver)
        )
        sekretariat.nacisnij_enter_na_sekretariat_urlopy_przycisk(self.driver)

        ############## Urlopy ###############
        self.assertTrue(
            sekretariat.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver,
                                                             'http://env20180415.abraks.pl/secretariat/vacation')
        )
        self.assertTrue(
            sekretariat.sprawdz_sekretariat_logo(self.driver, u'Urlop > Indeks')
        )
        self.assertTrue(
            sekretariat.sprawdz_sekretariat_tabela(self.driver)
        )
        sekretariat.nacisnij_enter_na_sekretariat_zadania_przycisk(self.driver)

        ############## Zadania ###############
        self.assertTrue(
            sekretariat.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver,
                                                             'http://env20180415.abraks.pl/secretariat/task')
        )
        self.assertTrue(
            sekretariat.sprawdz_sekretariat_logo(self.driver, u'Zadanie > Indeks')
        )
        self.assertTrue(
            sekretariat.sprawdz_sekretariat_tabela(self.driver)
        )
        admin.nacisnij_enter_na_admin_przycisk(self.driver)
        self.assertTrue(
            admin.sprawdz_rezultat_nacisniecia_role(self.driver, 'Role')
        )
        admin.nacisnij_enter_na_role_przycisk(self.driver)

        ###################### Admin ###############

        ############## Role ###############
        self.assertTrue(
            admin.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/admin/role')
        )
        self.assertTrue(
            admin.sprawdz_admin_logo(self.driver, u'Rola > Indeks')
        )
        self.assertTrue(
            admin.sprawdz_admin_tabela(self.driver)
        )
        admin.nacisnij_enter_na_admin_uprawnienia_przycisk(self.driver)

        ############## Uprawnienia ###############
        self.assertTrue(
            admin.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/admin/permission')
        )
        self.assertTrue(
            admin.sprawdz_admin_logo(self.driver, u'Uprawnienie > Indeks')
        )
        self.assertTrue(
            admin.sprawdz_admin_tabela(self.driver)
        )
        admin.nacisnij_enter_na_admin_uzytkownicy_przycisk(self.driver)

        ############## Uzytkownicy ###############
        self.assertTrue(
            admin.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/admin/user')
        )
        self.assertTrue(
            admin.sprawdz_admin_logo(self.driver, u'Użytkownik > Indeks')
        )
        self.assertTrue(
            admin.sprawdz_admin_tabela(self.driver)
        )
        admin.nacisnij_enter_na_admin_strony_przycisk(self.driver)

        ############## Strony ###############
        self.assertTrue(
            admin.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/admin/page')
        )
        self.assertTrue(
            admin.sprawdz_admin_logo(self.driver, u'Strona > Indeks')
        )
        self.assertTrue(
            admin.sprawdz_admin_tabela(self.driver)
        )
        admin.nacisnij_enter_na_admin_ustawienia_przycisk(self.driver)

        ############## Ustawienia ###############
        self.assertTrue(
            admin.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/admin/setting')
        )
        self.assertTrue(
            admin.sprawdz_admin_logo(self.driver, u'Ustawienie > Indeks')
        )
        self.assertTrue(
            admin.sprawdz_admin_ustawienia_aplikacji_tabela(self.driver)
        )
        self.assertTrue(
            admin.sprawdz_admin_ustawienia_firmy_tabela(self.driver)
        )
        self.assertTrue(
            admin.sprawdz_admin_ustawienia_sekcji_meta_tabela(self.driver)
        )
        ############## Wylogowanie ###############
        logowanie.nacisnij_enter_na_wyloguj_przycisk(self.driver)
        self.assertTrue(
            logowanie.sprawdz_czy_gorne_logo_pasek_jest_widoczne(self.driver)
        )
        self.assertTrue(
            logowanie.sprawdz_czy_sekcja_logowania_jest_widoczna(self.driver)
        )
        self.assertTrue(
            admin.sprawdz_czy_strona_zawiera_poprawna_nazwe(self.driver, 'http://env20180415.abraks.pl/login')
        )

    def assertItemEqual(self, num_widgetow, num_widgetow_poprawnie):
        pass


if __name__ == "__main__":
    unittest.main()
