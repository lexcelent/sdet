import datetime

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions

from base.base import Base


class ListTxPage(Base):

    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/listTx'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    transactions_table = '//table[@class="table table-bordered table-striped"]/tbody'

    # Getters
    def get_transactions_table(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.transactions_table)))

    def get_transactions_table_rows(self):
        table = self.get_transactions_table()
        return table.find_elements(By.TAG_NAME, 'tr')

    def get_transactions_table_cells(self):
        return self.get_transactions_table().find_elements(By.TAG_NAME, 'td')

    def get_transactions_table_rows_count(self):
        return len(self.get_transactions_table_rows())

    # Actions
    def save_table_as_csv(self):
        self.make_csv(self.get_transactions_table_rows())

    # Methods
    def save_csv(self):
        with allure.step("Save as csv"):
            table = self.prepare_for_csv(self.get_transactions_table_cells())
            self.make_csv(table)
