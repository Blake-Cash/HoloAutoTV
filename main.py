#Selenium for Web Driving
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Time for waiting to redirect
import time

#Requests for querying holotools
import requests

#Random for picking random active stream
import random

url = "https://api.holotools.app/v1/live?hide_channel_desc=1&max_upcoming_hours=1&lookback_hours=0"
path_to_h264ify = "/home/pi/HoloAutoTV/1.1.0_1"

def getDestination():
    print ('Fetching new stream...')
    response = requests.get(url)
    parsedResponse = (response.json())
    liveChannels = (parsedResponse["live"])
    amtOfChannelsLive = len(liveChannels)
    selectedChannelNumber = random.randint(0, amtOfChannelsLive-1)
    selectedChannel = liveChannels[selectedChannelNumber]
    return selectedChannel['yt_video_key']

def start_browser():
    print ('Initializing browser...')
    chrome_options = Options()
    chrome_options.add_argument('load-extension=' + path_to_h264ify)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver

def navigateTo(driver, destination):
    print('Navigating to stream...')
    driver.get('https://youtube.com/watch?v=' + destination)
    time.sleep(3600)

print ('Starting HoloAutoTV...')
driver = start_browser()
while True:
    destination = getDestination()
    navigateTo(driver, destination)
