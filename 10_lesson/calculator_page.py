from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    """Page Object для калькулятора с медленными вычислениями."""

    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.

        Args:
            driver (webdriver.Chrome): Экземпляр Selenium WebDriver
        """
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CLASS_NAME, "screen")
        self.button_locator = "//span[text()='{}']"

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """Открывает URL с калькулятором в браузере."""
        url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        self.driver.get(url)

    @allure.step("Установить задержку вычислений: {seconds} секунд")
    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает время задержки вычислений.

        Args:
            seconds (int): Время задержки в секундах
        """
        self.driver.find_element(*self.delay_input).clear()
        self.driver.find_element(*self.delay_input).send_keys(str(seconds))

    @allure.step("Нажать кнопку: '{button_text}'")
    def click_button(self, button_text: str) -> None:
        """
        Кликает по указанной кнопке калькулятора.

        Args:
            button_text (str): Текст на кнопке (цифры или операции)
        """
        locator = (By.XPATH, self.button_locator.format(button_text))
        self.driver.find_element(*locator).click()

    @allure.step("Получить результат вычислений (таймаут: {timeout} сек)")
    def get_result(self, timeout: int = 50) -> str:
        """
        Ожидает и возвращает результат вычислений.

        Args:
            timeout (int): Максимальное время ожидания в секундах

        Returns:
            str: Текст результата на экране калькулятора
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.screen, "15")
        )
        return self.driver.find_element(*self.screen).text
