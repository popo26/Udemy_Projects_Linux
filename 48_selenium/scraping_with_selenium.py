from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver = "/home/popo26/Documents/_Udemy/chrome_driver/chromedriver"
ser = Service(chrome_driver)
driver = webdriver.Chrome(service=ser)

driver.get("https://www.python.org/")

# price = driver.find_element(By.CLASS_NAME, "a-offscreen")
# print(price.get_attribute('innerHTML')) # I couldnt get text with "price.text"

dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
events = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu a")

dictionary = {}
for n in range(len(dates)):
    dictionary[n] = {
        "date" : dates[n].text,
        "name" : events[n].text
    }
print(dictionary)

# date_list = []
# for date in dates:
#     date_list.append(date.get_attribute("datetime"))
# print(date_list)
# print(type(date_list[0]))

# date_list2 = []
# for d in date_list:
#     if d and d.endswith("T00:00:00+00:00"):
#         x = d.strip("T00:00:00+00:00")
#         date_list2.append(x)
#         # print(x)
#     elif d and d.endswith("T16:00:00+00:00"):
#         x = d.strip("T16:00:00+00:00")
#         date_list2.append(x)
#         # print(x)
#     elif d and d.endswith("T16:30:00+00:00"):
#         x = d.strip("T16:30:00+00:00")
#         date_list2.append(x)
#         # print(x)
# print(date_list2)

# e_list = []
# for e in events:
#     event = e.text
#     e_list.append(event)
# print(e_list)

# # e_dict = {}
# # for event in events:
# #     e_dict["name"]= event.text
# #     print(e_dict)
# #     e_dict

# # dictionary = {}
# # for i in range(len(e_list)):
# #     dictionary[date_list2[i]] = e_list[i]
# # print(dictionary)










# driver.close() #closes a single tab
driver.quit() #closes entire browser