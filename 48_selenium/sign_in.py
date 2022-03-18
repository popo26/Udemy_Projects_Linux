from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver = "/home/popo26/Documents/_Udemy/chrome_driver/chromedriver"
ser = Service(chrome_driver)
driver = webdriver.Chrome(service=ser)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("POPO")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("TATA")
email = driver.find_element(By.NAME, "email")
email.send_keys("test@test.com")
email.send_keys(Keys.ENTER)

# driver.quit()