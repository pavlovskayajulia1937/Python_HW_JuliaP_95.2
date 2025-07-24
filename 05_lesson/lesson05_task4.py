# Форма авторизации
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/login")
username = driver.find_element(By.XPATH, '//input[@type="text"]')
password = driver.find_element(By.XPATH, '//input[@type="password"]')
username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")
sleep(10)
driver.find_element(By.XPATH, '//button[@type="submit"]').click()
sleep(10)
green_element = driver.find_element(By.XPATH, '//img')
print(green_element.get_property("alt"))

driver.quit()