import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class CustomerPage:

    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer'

    def __init__(self, driver):
        self.driver = driver

    # Locators
    combobox_user_select = 'userSelect'
    button_login = '//button[@class="btn btn-default"]'

    # Getters
    def get_select_user(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.combobox_user_select)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    # Actions
    def select_user_by_value(self, value: str):
        select = Select(self.get_select_user())
        select.select_by_value(value)

    def click_button_login(self):
        self.get_button_login().click()

    # Methods
    def select_harry_potter(self):
        with allure.step("Select Harry Potter and Click Login"):
            self.select_user_by_value('2')
            self.click_button_login()
