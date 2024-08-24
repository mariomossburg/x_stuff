
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
import config

# possible argument search_term
def search_group(group_name):
    driver = config.get_driver()

    time.sleep(1)

    tabs = driver.find_elements(By.XPATH, "//a[@role='tab']")

    for index,tab in enumerate(tabs):

        span = tab.find_element(By.XPATH, ".//span")

        span_text = span.text.lower()

        print(f"Tab '{index}': '{span_text}'")

        if span_text == group_name:
            tab.click()
            print(f"Clicked tab {index}: '{span_text}'")

            break

# search_group(group_name="following")


# search_group()