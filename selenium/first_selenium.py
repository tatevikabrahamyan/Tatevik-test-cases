from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager  
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://v2.zynq360.com/")
print("Application title is ", driver.title)
time.sleep(2)

email = driver.find_element_by_id("emailAddress")
password = driver.find_element_by_id("loginPassword")
email.send_keys("suren.guyumjyan@insiso.co.uk")
time.sleep(2)
password.send_keys("Guyumsur12345^")
time.sleep(2)
driver.find_element_by_css_selector (".login-types button[type='submit']").click()
time.sleep(2)
driver.quit()