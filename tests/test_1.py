import datetime
import time
import allure

from selenium import webdriver

from pages.account import AccountPage
from pages.customer import CustomerPage
from pages.listTx import ListTxPage
from pages.login import LoginPage


@allure.description("Test 1")
def test_1():
    driver = webdriver.Firefox()

    login = LoginPage(driver)
    login.authorization_customer()

    customer = CustomerPage(driver)
    customer.select_harry_potter()

    # Здесь небольшая недоработка. Слишком неудобно написано
    account = AccountPage(driver)
    account.deposit_money()
    fibo_value = account.get_fibonacci(datetime.datetime.today().day + 1)
    account.check_balance_value(str(fibo_value))
    account.withdraw_money()
    account.check_balance_value('0')
    time.sleep(1)
    account.click_button_transactions()

    listTx = ListTxPage(driver)
    listTx.assert_value(listTx.get_transactions_table_rows_count(), 2)
    listTx.save_csv()

    driver.quit()
