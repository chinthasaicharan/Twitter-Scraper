import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver
import lxml
# Using normal input to gather the username
username= input('Enter the Twitter Username you want to scrap : ')

profile_url = f'https://twitter.com/{username}'

# Used Selenium web driver to extract source code since Twitter is asking for a JavaScrict enabled browser
chrome_path = "C:/selenium/chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

driver.get(url=profile_url)
# used time.sleep so that it waits until website is loaded . the function "implicitly_wait()" is not working properly
time.sleep(10)

soup = BeautifulSoup(driver.page_source,'lxml')

# scraped a script file from the webpage containing all the info of the user
# found all scripts in the webpage

all_scripts = soup.find_all('script')

# found our required script and it is in the form of JSON so converted to python dictionary

dict = json.loads(all_scripts[2].text)

# gathered data into a dictionary or JSON format

data_json = {
    'username': dict['author']['additionalName'],
    'description': dict['author']['description'],
    'original_Name': dict['author']['givenName'],
    'id': dict['author']['identifier'],
    'follower_count': dict['author']['interactionStatistic'][0]['userInteractionCount'],
    'following_count': dict['author']['interactionStatistic'][1]['userInteractionCount'],
    'tweet_count': dict['author']['interactionStatistic'][2]['userInteractionCount']
}
print(data_json)