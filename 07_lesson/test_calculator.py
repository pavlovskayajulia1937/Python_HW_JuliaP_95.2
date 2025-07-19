import pytest
import time
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_slow_calculator(browser):
    calc_page = CalculatorPage(browser)
    calc_page.open()
    calc_page.set_delay(45)
    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")
    start_time = time.time()
    result = calc_page.get_result()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Результат появился через {0:.2f} секунд".format(elapsed_time))
    assert result == "15", "Неверный результат вычислений"
    assert 44 <= elapsed_time <= 46, (
        "Результат появился через {0} вместо 45 сек".format(elapsed_time)
    )
