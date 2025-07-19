import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def browser():
    options = Options()
    service = Service(executable_path="geckodriver")
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()


def test_checkout_total_price(browser):
    # Инициализация страниц
    login_page = LoginPage(browser)
    products_page = ProductsPage(browser)
    cart_page = CartPage(browser)
    checkout_page = CheckoutPage(browser)

    # 1. Авторизация
    browser.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    # 2. Добавление товаров
    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    for product in products:
        products_page.add_product_to_cart(product)

    # 3. Переход в корзину и оформление
    products_page.go_to_cart()
    cart_page.proceed_to_checkout()

    # 4. Заполнение данных
    checkout_page.fill_checkout_info("Юлия", "Павловская", "194363")

    # 5. Проверка суммы
    total = checkout_page.get_total_amount()
    assert "Total: $58.29" in total, (
        f"Ожидалось 'Total: $58.29', получено '{total}'"
    )
