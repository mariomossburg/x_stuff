from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import config
import time 


def make_post(post_content="anothertest"):

    driver = config.get_driver()

    url = "https://x.com/home"

    driver.get(url)
    # time.sleep(8)

    try:
        wait = WebDriverWait(driver,2)
        write_post = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div[contenteditable='true'][data-testid='tweetTextarea_0']")
            )
        )
        write_post.click()
        write_post.send_keys(post_content)

        submit_post = driver.find_element(By.CSS_SELECTOR, "button[data-testid='tweetButtonInline']")
        submit_post.click()
    except:
        print("element not found")

# make_post()

