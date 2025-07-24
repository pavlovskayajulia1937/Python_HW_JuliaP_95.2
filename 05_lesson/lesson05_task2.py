# Клик по кнопке без ID
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/dynamicid")
sleep(10)
driver.find_element(By.XPATH,"//button[contains(concat(' ', normalize-space(@class)), ' btn-primary')]").click()

sleep(10)