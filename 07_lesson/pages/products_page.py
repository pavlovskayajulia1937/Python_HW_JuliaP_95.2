from selenium.webdriver.common.by import By


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart(self, product_name):
        xpath = (
            f"//div[text()='{product_name}']"
            "/ancestor::div[@class='inventory_item']"
            "//button"
        )
        self.driver.find_element(By.XPATH, xpath).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()
