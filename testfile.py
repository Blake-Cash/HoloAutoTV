import selenium
from selenium import webdriver

import time
import requests

url = "https://api.holotools.app/v1/live"

def navigateTo():
    driver = webdriver.Chrome()
    driver.get('https://twitter.com/home')

print ('Starting HoloTV')
response = requests.get(url)
print (response.json())
navigateTo()