from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage:

    # URL
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'

    def __init__(self, driver):
        self.driver = driver

    # Locators
    button_customer_login = '//button[@ng-click="customer()"]'
    button_bank_manager_login = '//button[@ng-click="manager()"]'

    # Getters
    def get_button_customer_login(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_customer_login)))

    # Actions
    def click_button_customer_login(self):
        self.get_button_customer_login().click()

    # Methods
    def authorization_customer(self):
        with allure.step("Authorization button"):
            self.driver.get(self.url)
            self.click_button_customer_login()

