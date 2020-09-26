#Selenium for Web Driving
import selenium
from selenium import webdriver

#Time for waiting to redirect
import time

#Requests for querying holotools
import requests

#Random for picking random active stream
import random

url = "https://api.holotools.app/v1/live?hide_channel_desc=1&max_upcoming_hours=1&lookback_hours=0"

def getDestination():
    response = requests.get(url)
    parsedResponse = (response.json())
    liveChannels = (parsedResponse["live"])
    amtOfChannelsLive = len(liveChannels)
    selectedChannelNumber = random.randint(0, amtOfChannelsLive-1)
    selectedChannel = liveChannels[selectedChannelNumber]
    return selectedChannel['yt_video_key']

def navigateTo(destination):
    driver = webdriver.Chrome()
    driver.get('https://youtube.com/watch?v=' + destination)
    time.sleep(3600)

print ('Starting HoloTV!')
while True:
    destination = getDestination()
    navigateTo(destination)
