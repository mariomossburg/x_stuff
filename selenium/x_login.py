# https://selenium-python.readthedocs.io/getting-started.html
from selenium.webdriver.common.by import By
import config
import time 

# create try/if/else for if extra feild appears 


def login():
    driver = config.get_driver()

    url = "https://x.com/login"

    driver.get(url)
    driver.maximize_window()

    time.sleep(3)

    username = driver.find_element(By.XPATH, "//input[@name='text']")
    username.send_keys(config.username)

    click_next = driver.find_element(By.XPATH, "//button[@role='button' and @type='button' and .//span[text()='Next']]")
    click_next.click()
    time.sleep(2)

    password = driver.find_element(By.XPATH, "//input[@type='password' and @name='password']")
    password.click()
    password.send_keys(config.password)

    submit = driver.find_element(By.XPATH, "//button[@data-testid='LoginForm_Login_Button' and @role='button' and contains(., 'Log in')]")
    submit.click()
    

login()