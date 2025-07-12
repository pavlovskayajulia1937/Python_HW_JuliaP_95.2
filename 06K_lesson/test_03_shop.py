from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
service = Service(executable_path="geckodriver")
driver = webdriver.Firefox(service=service, options=firefox_options)

try:
    driver.get("https://www.saucedemo.com/")
    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Добавление товаров
    items = [
        "Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"
        ]
    for item in items:
        xpath = (
            f"//div[text()='{item}']"
            "/ancestor::div[@class='inventory_item']"
            "//button"
        )
        driver.find_element(By.XPATH, xpath).click()

    # Оформление заказа
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    # Заполнение формы
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Иванов")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

    # Проверка итоговой суммы
    total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_element.text

    assert "Total: $58.29" in total_text, (
        f"Ожидалось 'Total: $58.29', получено '{total_text}'"
    )

finally:
    driver.quit()
