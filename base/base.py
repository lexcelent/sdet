import datetime
import pandas as pd


class Base:
    def __init__(self, driver):
        self.driver = driver

    def fibonacci(self, n):
        if n in (1, 2):
            return 1
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def assert_webelement_value(self, value, expected_value):
        assert value.text == expected_value

    def assert_value(self, value, expected_value):
        assert value == expected_value

    def make_csv(self, data):
        columns = ['DateTime', 'Amount', 'Transaction']

        df = pd.DataFrame(data, columns=columns)
        df.to_csv(r'../test_results/transactions.csv', index=False)

    def prepare_for_csv(self, table):
        """Функция для преобразования таблицы в формат, пригодный для .csv по заданию"""
        new_data = []
        for i in range(0, len(table), 3):
            row = []
            new_datetime = datetime.datetime.strptime(table[i].text, '%b %d, %Y %H:%M:%S %p')
            new_datetime_str = new_datetime.strftime('%d %m %Y %H:%M:%S')
            row.append(new_datetime_str)
            row.append(table[i + 1].text)
            row.append(table[i + 2].text)
            new_data.append(row)
        return new_data
