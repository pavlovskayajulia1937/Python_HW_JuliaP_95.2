# Поле ввода
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/inputs")
search_box = driver.find_element(By.XPATH, '//input[@type="number"]')
search_box.send_keys("Sky")
sleep(10)
search_box.clear()
search_box.send_keys("Pro")
sleep(10)

# driver.quit()