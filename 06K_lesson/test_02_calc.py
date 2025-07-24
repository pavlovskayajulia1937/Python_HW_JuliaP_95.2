import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    """Фикстура для инициализации и закрытия браузера."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_slow_calculator(browser):
    """Тест медленного калькулятора с задержкой 45 секунд."""
    # Открытие страницы
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    # Установка задержки в 45 секунд
    delay_input = browser.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажатие кнопок 7 + 8 =
    browser.find_element(By.XPATH, "//span[text()='7']").click()
    browser.find_element(By.XPATH, "//span[text()='+']").click()
    browser.find_element(By.XPATH, "//span[text()='8']").click()
    browser.find_element(By.XPATH, "//span[text()='=']").click()

    # Ожидание результата в течение 45 секунд
    start_time = time.time()
    WebDriverWait(browser, 50).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )
    end_time = time.time()

    # Проверка результата
    elapsed_time = end_time - start_time
    print("Результат появился через {0:.2f} секунд".format(elapsed_time))

    assert 44 <= elapsed_time <= 46, (
        "Результат не через 45 секунд, а через {0}".format(elapsed_time)
    )
