import config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





def like_post():
    driver = config.get_driver()

    # like_post = driver.find_element(By.XPATH, "//button[@data-testid='like']")
    # like_post.click()
    try:
        wait = WebDriverWait(driver,5)
        like_post = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@data-testid='like']")
            )
        )
        like_post.click()
    except Exception as e:
        print(f"Error: {e}")


# like_post()
