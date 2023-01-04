from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time


def click_all_questions(driver: webdriver.Chrome):
	for i in range(2, 47):
		firstAlternative = driver.find_element(By.XPATH, f'//*[@id="ays_finish_quiz_4"]/div[{i}]/div/div[3]/div[1]/label[1]')
		try:
			firstAlternative.click()
		except ElementClickInterceptedException:
			print("failed click, retrying")
			time.sleep(.3)
			firstAlternative.click()
		
		nesteBtn = driver.find_element(By.XPATH, f'//*[@id="ays_finish_quiz_4"]/div[{i}]/div/div[4]/input[2]')
		nesteBtn.click()

def get_img_url(driver: webdriver.Chrome, questionNum: int):
	xPath = f'//*[@id="ays_finish_quiz_4"]/div[48]/div[{questionNum}]/div/div[2]/img'
	image_element = driver.find_element(By.XPATH, xPath)

	return image_element.get_attribute('src') # type: ignore

def get_answers_from_number(questionNum: int, driver: webdriver.Chrome) -> tuple[list[str], int]:
	answers: list[WebElement] = []
	correctAnswer = -1
	for j in range(4):
		xPath = f'//*[@id="ays_finish_quiz_4"]/div[48]/div[{questionNum}]/div/div[3]/div[{j + 1}]/label[1]'
		answers.append(driver.find_element(By.XPATH, xPath))

	for i, answer in enumerate(answers) :
		answerClass: str = answer.get_attribute('class') # type: ignore
		if 'correct' in answerClass: correctAnswer = i + 1

	answersStr = [i.get_attribute("textContent") for i in answers] # type: ignore

	return  answersStr, correctAnswer

def get_question_title(questionNum: int, driver: webdriver.Chrome) -> str:
	title = driver.find_element(By.XPATH, f'//*[@id="ays_finish_quiz_4"]/div[48]/div[{questionNum}]/div/div[1]/h3')

	return title.get_attribute("innerHTML") # type: ignore

def get_all_questions(driver: webdriver.Chrome):
	questions: list[object] = []

	for i in range(1, 46):
		try:
			title = get_question_title(i, driver)
		except:
			print(f"Failed read title index:{i}")
			time.sleep(2)
			title = get_question_title(i, driver)
		answers, correctAnswer = get_answers_from_number(i, driver)
		image_url = get_img_url(driver, i)

		questions.append({
			'title': title,
			'image_url': image_url,
			'answers': answers,
			'correct_answer': correctAnswer 
		})

	return questions

def do_login(driver: webdriver.Chrome):
	with open('bilteoriCreds.json', 'r') as f:
		creds = json.load(f)

	acceptCookieBtn = driver.find_element(By.ID, "daextlwcnf-cookie-notice-button-2")

	acceptCookieBtn.click()

	time.sleep(1)

	usernameInput = driver.find_element(By.ID, "username")
	usernameInput.send_keys(creds['username']) # type: ignore

	passwordInput = driver.find_element(By.ID, "password")
	passwordInput.send_keys(creds['password']) # type: ignore

	time.sleep(1)
	loginBtn = driver.find_element(By.NAME, "login")
	loginBtn.click()

	# time.sleep(4)

def start_del_1_pensum(driver: webdriver.Chrome):
	
	pensumBtn = driver.find_element(By.XPATH, '//*[@id="kt-info-box_6a17bf-53"]/a')
	pensumBtn.click()

	startDel1Btn = driver.find_element(By.XPATH, '//*[@id="ays_finish_quiz_6"]/div[1]/div/div/div/input')
	startDel1Btn.click()

def start_eksamen(driver: webdriver.Chrome):
	eksamenBtn = driver.find_element(By.XPATH, '//*[@id="kt-info-box_432379-12"]')
	eksamenBtn.click()

	startEksamenBtn = driver.find_element(By.XPATH, '//*[@id="ays_finish_quiz_4"]/div[1]/div/div/div/input')
	startEksamenBtn.click()
	

def main():
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
	driver.get("https://www.bil-teori.no/min-konto/")

	time.sleep(3)

	do_login(driver)
	start_eksamen(driver)

	time.sleep(3)

	click_all_questions(driver)

	print("Loading questions")
	time.sleep(10)

	with open('out.json', 'r') as f:
		questions: list[object] = json.load(f)
		
	questions.extend(get_all_questions(driver))

	with open('out.json', 'w+', encoding='utf8') as f:
		f.write(json.dumps(questions))

	print("Questions saved")

	driver.quit()

	main()


if __name__ == '__main__':
	main()