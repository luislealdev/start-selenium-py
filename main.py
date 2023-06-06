from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/luisleal/development"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu li time")
names = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu li a")
dictionary = {}

for i in range(len(names)):
    dictionary[i] = {'time:': dates[i].text, 'name': names[i].text}

print(dictionary)

driver.close()
