from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))

driver.get
("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

driver.implicitly_wait(25)
picture = driver.find_element(By.ID, "award")
print(picture.get_attribute("src"))

blue_button = driver.find_element(By.ID, "updatingButton")
blue_button.click()
text = blue_button.text
print(text)
