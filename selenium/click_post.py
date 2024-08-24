import config
# import search
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click_post(post_element):
#     time.sleep(10)
    driver = config.get_driver()
    driver.maximize_window()
    

    try:
        wait = WebDriverWait(driver,8)
        click_post = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//article[@data-testid="tweet"]')
            )
        )
        click_post.click()
    except Exception as e:
        print(f"Error: {e}")

# click_post(post="idk")






# def _like_post_reply_follow();
#         find_post()

        # search_term = "connect"
        # search.search_with_query(search_term)






# def 