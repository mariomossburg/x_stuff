import config 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def follow_button_check():
    driver = config.get_driver()

    click_menu = driver.find_element(By.XPATH, "//button[@data-testid='caret' and @aria-haspopup='menu']")
    click_menu.click()
    time.sleep(1)

    follow_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Follow') or contains(text(), 'Unfollow')]")
    button_text = follow_button.text 
    print(button_text)

    if "Follow" in button_text:
            is_following = False
            print("not followed")
            follow_button.click()
    else:
            print("we follow")
            is_following = True

    # try:
    #     ActionChains(driver).move_to_element(driver.find_element(By.TAG_NAME, 'body')).click().perform()
    # except Exception as e:
    #     print(f"Error closing menu: {e}")

    return is_following


# follow_button_check()