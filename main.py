from selenium import webdriver

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.bil-teori.no/min-konto/")
print(driver.title)


input("")