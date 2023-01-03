from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time

def getQuestions(driver: webdriver.Chrome) :
	questions: list[WebElement] = []
	for i in range(4):
		questions.append(driver.find_element(By.XPATH, f'//*[@id="ays_finish_quiz_6"]/div[2]/div/div[3]/div[{i + 1}]/label[1]'))# type: ignore

	return [i.text for i in questions] # type: ignore
with open('bilteoriCreds.json', 'r') as f:
	creds = json.load(f)
	print(creds)

from selenium import webdriver


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.bil-teori.no/min-konto/")

time.sleep(3)

acceptCookieBtn = driver.find_element(By.ID, "daextlwcnf-cookie-notice-button-2")

acceptCookieBtn.click()

time.sleep(1)

usernameInput = driver.find_element(By.ID, "username")
usernameInput.send_keys(creds['username']) # type: ignore
print(type(usernameInput))

passwordInput = driver.find_element(By.ID, "password")
passwordInput.send_keys(creds['password']) # type: ignore

time.sleep(1)
loginBtn = driver.find_element(By.NAME, "login")
loginBtn.click()

time.sleep(4)

pensumBtn = driver.find_element(By.XPATH, '//*[@id="kt-info-box_6a17bf-53"]/a')
pensumBtn.click()

time.sleep(4)

startDel1Btn = driver.find_element(By.XPATH, '//*[@id="ays_finish_quiz_6"]/div[1]/div/div/div/input')
startDel1Btn.click()

time.sleep(5)
questions = getQuestions(driver)
for i in questions:
	print(i)


input("")