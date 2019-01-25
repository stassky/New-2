from selenium import webdriver

import time


driver = webdriver.Firefox(executable_path="D:\Selenium\geckodriver.exe")
driver.get("http://192.168.99.100:5000")
driver.implicitly_wait(10)



# FIND ELEMENT AND PRINT IT (READ)