from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

c = webdriver.ChromeOptions()
c.add_argument("--incognito")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options =c)
driver.get('https://www.reddit.com/r/Eldenring/')
time.sleep(2)

driver.find_element_by_css_selector('#SHORTCUT_FOCUSABLE_DIV > div:nth-child(2) > header > div > div._2u8LqkbMtzd0lpblMFbJq5 > div > div._1JBkpB_FOZMZ7IPr3FyNfH > a._3Wg53T10KuuPmyWOMWsY2F._2iuoyPiKHN3kfOoeIQalDT._2tU8R9NTqhvBrhoNAXWWcP.HNozj_dKjQZ59ZsfEegz8._2nelDm85zKKmuD94NequP0').click()
time.sleep(2)
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
time.sleep(2)
email = driver.find_element_by_css_selector('#loginUsername')
email.send_keys(username)
login = driver.find_element_by_css_selector('#loginPassword')
login.send_keys(password)
time.sleep(3)
driver.find_element_by_css_selector('body > div > main > div.OnboardingStep.Onboarding__step.mode-auth > div > div.Step__content > form > fieldset:nth-child(8) > button').click()
time.sleep(5)
driver.find_element_by_css_selector("div[aria-label='upvote']").click()
