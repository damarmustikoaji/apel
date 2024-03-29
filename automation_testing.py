from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chromeDriver=Service('./chromedriver_linux64')
opts = Options()
opts.headless = True

browser = webdriver.Chrome(options=opts, service=chromeDriver)

try:
    browser.get('https://sebangsa.com')
    assert 'Sebangsa - Platform Aktivitas Komunitas' == browser.title
    print('TC - 001 Assert Browser Title [PASS]')
finally:
    browser.quit()
