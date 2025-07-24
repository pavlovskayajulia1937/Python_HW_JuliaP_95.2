from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))

driver.implicitly_wait(25)

driver.get("http://uitestingplayground.com/textinput")
input_box = driver.find_element(By.CLASS_NAME, "form-control")
input_box.send_keys("SkyPro")

blue_button = driver.find_element(By.ID, "updatingButton")
blue_button.click()
text = blue_button.text

print(text)

driver.quit()
