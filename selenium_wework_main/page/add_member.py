from time import sleep

from selenium.webdriver.common.by import By

from selenium_wework_main.page.base_page import BasePage


class AddMember(BasePage):

    def add_member(self):
        # sendkeys
        sleep(2)
        self.find(By.ID, 'username').send_keys("abcdefffff")
        self.find(By.ID, 'memberAdd_acctid').send_keys("abcdefffff")
        self.find(By.ID, 'memberAdd_acctid').send_keys("abcdefffff")
        self.find(By.ID, 'memberAdd_phone').send_keys("11111111111")
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        sleep(5)
        return True

    def get_member(self):
        elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        return [element.get_attribute("title") for element in elements]
