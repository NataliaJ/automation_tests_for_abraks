# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def poczekaj_na_widocznosc_elementu(driver_instance, xpath, time_to_wait=8):
    elem = WebDriverWait(driver_instance, time_to_wait).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )
    return elem


def poczekaj_na_widocznosc_elementu_po_logowaniu(driver_instance, xpath, time_to_wait=30):
    elem = WebDriverWait(driver_instance, time_to_wait).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )
    return elem


def poczekaj_na_widocznosc_wszystkich_elementow(driver_instance, xpath, time_to_wait=8):
    elems = WebDriverWait(driver_instance, time_to_wait).until(
        EC.visibility_of_all_elements_located((By.XPATH, xpath))
    )
    return elems


def poczekaj_na_obecnosc_elementu(driver_instance, xpath, time_to_wait=8):
    elem = WebDriverWait(driver_instance, time_to_wait).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    return elem


def wyslij_klucz_do_elementu(driver_instance, xpath, text):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=xpath
    )
    elem.send_keys(text)


def nacisnij_enter_na_elemencie(driver_instance, xpath):
    elem = poczekaj_na_widocznosc_elementu(
        driver_instance=driver_instance,
        xpath=xpath
    )
    elem.send_keys(Keys.RETURN)


def sprawdz_czy_strona_zawiera_poprawna_nazwe(driver_instance, text):
    url_text = driver_instance.current_url
    return url_text
