import config 
import time
from selenium.webdriver.common.by import By


def follow():
    driver = config.get_driver()

    click_menu = driver.find_element(By.XPATH, "//button[@data-testid='caret' and @aria-haspopup='menu']")
    click_menu.click()

    time.sleep(1)
    click_follow = driver.find_element(By.XPATH, "//span[starts-with(text(), 'Follow') and contains(text(), '@')]")
    click_follow.click()


# follow()


