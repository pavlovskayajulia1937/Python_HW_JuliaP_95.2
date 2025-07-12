from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    # Установка задержки в 45 секунд
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажатие кнопок 7 + 8 =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Ожидание результата в течение 45 секунд
    start_time = time.time()
    result = WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )
    end_time = time.time()

    # Проверка, что результат появился через ~45 секунд
    elapsed_time = end_time - start_time
    print("Результат появился через %.2f секунд" % elapsed_time)

    assert 44 <= elapsed_time <= 46, (
        "Результат не через 45 секунд, а через {}".format(elapsed_time)
        )
    print("Тест пройден успешно!")

finally:
    driver.quit()
