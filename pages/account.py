import datetime
import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions

from base.base import Base


class AccountPage(Base):

    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    button_transactions = '//button[@ng-class="btnClass1"]'
    button_deposit = '//button[@ng-class="btnClass2"]'
    button_withdraw = '//button[@ng-class="btnClass3"]'

    input_number = '//input[@type="number"]'
    button_submit = '//button[@type="submit"]'

    account_number = '//strong[@class="ng-binding"][1]'
    balance_value = '//strong[@class="ng-binding"][2]'
    currency = '//strong[@class="ng-binding"][3]'

    # Getters
    def get_fibonacci(self, n):
        return self.fibonacci(n)

    def get_button_transactions(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_transactions)))

    def get_button_deposit(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_deposit)))

    def get_button_withdraw(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_withdraw)))

    def get_input_number(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.input_number)))

    def get_button_submit(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_submit)))

    def get_balance_value(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.balance_value)))

    # Actions
    def click_button_transactions(self):
        self.get_button_transactions().click()

    def click_button_deposit(self):
        self.get_button_deposit().click()

    def click_button_withdraw(self):
        self.get_button_withdraw().click()

    def send_keys_to_input_number(self, amount):
        self.get_input_number().send_keys(str(amount))

    def click_button_submit(self):
        self.get_button_submit().click()

    # Methods
    def deposit_money(self):
        with allure.step("Deposit money"):
            fibo_value = self.get_fibonacci(datetime.datetime.today().day + 1)
            self.click_button_deposit()
            self.send_keys_to_input_number(fibo_value)
            self.click_button_submit()

    def withdraw_money(self):
        with allure.step("Withdraw money"):
            fibo_value = self.get_fibonacci(datetime.datetime.today().day + 1)
            self.click_button_withdraw()
            # StaleElementReferenceException
            # Можно обернуть в try except, если не забуду. Временное решение - задержка 2с
            time.sleep(2)
            self.send_keys_to_input_number(fibo_value)
            self.click_button_submit()

    def check_balance_value(self, expected_value):
        with allure.step("Check balance value"):
            self.assert_webelement_value(self.get_balance_value(), expected_value)