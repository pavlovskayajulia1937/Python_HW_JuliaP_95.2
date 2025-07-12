import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def browser():
    # Инициализация драйвера
    firefox_options = Options()
    service = Service(executable_path="geckodriver")
    driver = webdriver.Firefox(service=service, options=firefox_options)
    yield driver
    # Закрытие драйвера после теста
    driver.quit()


def test_checkout_total_price(browser):
    # 1. Открыть сайт
    browser.get("https://www.saucedemo.com/")

    # 2. Авторизация
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    # 3. Добавление товаров
    items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    for item in items:
        xpath = (
            f"//div[text()='{item}']"
            "/ancestor::div[@class='inventory_item']"
            "//button"
        )
        browser.find_element(By.XPATH, xpath).click()

    # 4. Оформление заказа
    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    browser.find_element(By.ID, "checkout").click()

    # 5. Заполнение формы
    browser.find_element(By.ID, "first-name").send_keys("Юлия")
    browser.find_element(By.ID, "last-name").send_keys("Павловская")
    browser.find_element(By.ID, "postal-code").send_keys("194363")
    browser.find_element(By.ID, "continue").click()

    # 6. Проверка итоговой суммы
    total = browser.find_element(By.CLASS_NAME, "summary_total_label").text
    assert "Total: $58.29" in total, (
        f"Ожидалось 'Total: $58.29', получено '{total}'"
    )
 
