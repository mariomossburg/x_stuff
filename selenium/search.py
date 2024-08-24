from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
import config

# possible argument search_term
def search_with_query(search_term):

    driver = config.get_driver()
    url = "https://x.com/home"

    driver.get(url)
    driver.maximize_window()

    time.sleep(1)
    # search = driver.find_element(By.XPATH, "//a[@href='/explore' and @aria-label='Search and explore' and @role='link']")
    # search.click()

    type = driver.find_element(By.XPATH, "//input[@placeholder='Search' and @type='text']")
    # additional xpath specificity:  and @aria-label='Search query'
    type.click()
    type.send_keys(search_term)
    type.send_keys(Keys.RETURN)


# search_with_query(search_term = "connect")
