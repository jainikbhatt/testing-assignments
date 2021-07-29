from selenium import webdriver
import pytest
from TestObjects.Objects import Object
from utilities.customeLogger import LogGen
import time


baseURL = 'https://www.redthreadinnovations.com/'

driver = webdriver.Chrome(r'C:\Users\Shree\PycharmProjects\Project\pythonProject\pythonProject\RTI_Test_Project\drivers\chromedriver.exe')
driver.maximize_window()
driver.get(baseURL)
title = driver.title
if title == 'Red Thread Innovations':
    assert True
else:
    assert False

driver = webdriver.Chrome(r'C:\Users\Shree\PycharmProjects\Project\pythonProject\pythonProject\RTI_Test_Project\drivers\chromedriver.exe')
driver.maximize_window()
driver.get(baseURL)
obj = Object(driver)
obj.setPartnerBtn()

element = driver.find_element_by_tag_name('h1')
print(element)
