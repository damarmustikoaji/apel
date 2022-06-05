from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

usernameValue = "damar"
passwordValue = "123qwe"

s = ".wdm/drivers/chromedriver/linux64/102.0.5005.61/chromedriver"

driver = webdriver.Chrome(service=s)
driver.get("https://sebangsa.com")
masuk = driver.find_element(By.ID, "dropbtn-login")
masuk.click()
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
username.send_keys(usernameValue)
password.send_keys(passwordValue)
password.send_keys(Keys.RETURN)
driver.close()