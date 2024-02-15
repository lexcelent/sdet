import pytest

from selenium import webdriver


@pytest.fixture
def set_up():
    print('start')
    yield
    print('finish')