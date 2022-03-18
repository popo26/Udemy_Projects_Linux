from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver = "/home/popo26/Documents/_Udemy/chrome_driver/chromedriver"
ser = Service(chrome_driver)
driver = webdriver.Chrome(service=ser)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

total_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(total_count.text)

# total_count.click()

all_portal = driver.find_element(By.LINK_TEXT, "All portals") #Finding text for ahchor tag then Click 
# all_portal.click()

search = driver.find_element(By.NAME, "search") #Typing
search.send_keys("Python") #Typing
search.send_keys(Keys.ENTER) #clicking ENTER key


# driver.quit()