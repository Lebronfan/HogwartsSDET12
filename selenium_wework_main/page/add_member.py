from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AddMember:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def add_member(self):
        # sendkeys
        sleep(2)
        self._driver.find_element(By.ID, 'username').send_keys("abcdefffff")
        self._driver.find_element(By.ID, 'memberAdd_acctid').send_keys("abcdefffff")
        self._driver.find_element(By.ID, 'memberAdd_phone').send_keys("11111111111")
        self._driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()
        sleep(5)
        return True

    def get_member(self):
        elements = self._driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        return [element.get_attribute("title") for element in elements]
