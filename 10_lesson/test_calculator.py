import pytest
import time
import allure
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def browser():
    """Фикстура для инициализации браузера.

    Yields:
        webdriver.Chrome: Экземпляр Chrome WebDriver
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.title("Тестирование калькулятора с задержкой")
@allure.description("Проверка работы калькулятора с задержкой")
@allure.feature("Медленные вычисления")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator(browser):
    """Проверяет корректность работы калькулятора с задержкой.

    Тестирует:
    1. Правильность вычислений
    2. Соответствие времени выполнения установленной задержке
    """
    calc_page = CalculatorPage(browser)

    with allure.step("Подготовка теста"):
        calc_page.open()
        calc_page.set_delay(45)

    with allure.step("Выполнение операции 7 + 8"):
        calc_page.click_button("7")
        calc_page.click_button("+")
        calc_page.click_button("8")
        calc_page.click_button("=")

    with allure.step("Измерение времени выполнения"):
        start_time = time.time()
        result = calc_page.get_result()
        end_time = time.time()
        elapsed_time = end_time - start_time

    with allure.step("Запись времени выполнения"):
        time_msg = f"Время выполнения: {elapsed_time:.2f} сек"
        allure.attach(
            time_msg,
            name="Время выполнения",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("Проверка результатов"):
        with allure.step("Проверка вычислений"):
            expected = "15"
            assert result == expected, (
                f"Ожидалось {expected}, получено {result}"
            )

        with allure.step("Проверка времени"):
            time_out_of_range = (
                f"Время {elapsed_time:.2f} сек "
                f"вне диапазона 44-46 сек"
            )
            assert 44 <= elapsed_time <= 46, time_out_of_range
