from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

c = webdriver.ChromeOptions()
c.add_argument("--incognito")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options =c)
driver.get('https://www.spotify.com/us/')
