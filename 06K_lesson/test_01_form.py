import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    """Фикстура для инициализации и закрытия браузера."""
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Edge(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def test_data():
    """Фикстура с тестовыми данными для формы."""
    return {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }


def test_form_validation(browser, test_data):
    """Тест валидации формы с проверкой подсветки полей."""
    # Открытие страницы
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    # Заполнение формы
    for field, value in test_data.items():
        browser.find_element(
            By.CSS_SELECTOR, f'input[name="{field}"]'
            ).send_keys(value)

    # Отправка формы
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Проверка подсветки полей
    zip_code = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'input[name="zip-code"].alert-danger')
        )
    )
    assert "alert-danger" in zip_code.get_attribute("class"), (
        "Поле zip-code должно быть подсвечено красным"
    )

    for field in test_data.keys():
        element = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, f'input[name="{field}"].alert-success')
            )
        )
        assert "alert-success" in element.get_attribute("class"), (
            f"Поле {field} должно быть подсвечено зеленым"
        )


@pytest.mark.parametrize("field,value", [
    ("first-name", "Мария"),
    ("last-name", "Иванова"),
    ("e-mail", "another@test.com"),
])
def test_parametrized_form(browser, field, value):
    """Параметризованный тест для проверки разных значений полей."""
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )
    input_field = browser.find_element(
        By.CSS_SELECTOR, f'input[name="{field}"]'
        )
    input_field.clear()
    input_field.send_keys(value)
