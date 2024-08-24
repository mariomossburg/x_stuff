from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# run in terminal on local machine: 
# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222

username = ""
password = ""

def get_driver():

    chrome_options = Options()
    chrome_options.debugger_address = 'localhost:9222'

    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    return driver

# def clear_cache(driver):
#     driver.get('chrome://settings/clearBrowserData') 