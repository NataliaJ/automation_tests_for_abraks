# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def wait_for_visibility_of_element(driver_instance, xpath, time_to_wait=5):
    elem = WebDriverWait(driver_instance, time_to_wait).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )
    return elem

def wait_for_visibility_of_element_after_login(driver_instance, xpath, time_to_wait=30):
    elem = WebDriverWait(driver_instance, time_to_wait).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )
    return elem

def wait_for_visibility_of_all_elements(driver_instance, xpath, time_to_wait=8):
    elems = WebDriverWait(driver_instance, time_to_wait).until(
        EC.visibility_of_all_elements_located((By.XPATH, xpath))
    )
    return elems


def wait_for_presence_of_element(driver_instance, xpath, time_to_wait=8):
    elem = WebDriverWait(driver_instance, time_to_wait).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    return elem


def send_keys_to_element(driver_instance, xpath, text):
    elem = wait_for_visibility_of_element(
        driver_instance=driver_instance,
        xpath=xpath
    )
    elem.send_keys(text)


def click_enter_on_element(driver_instance, xpath):
    elem = wait_for_visibility_of_element(
        driver_instance=driver_instance,
        xpath=xpath
    )
    elem.send_keys(Keys.RETURN)


def check_url_contains_correct_name_page(driver_instance, text):
    url_text = driver_instance.current_url
    return url_text