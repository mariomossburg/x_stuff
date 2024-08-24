import config
import time
from selenium.webdriver.common.by import By



def comment_post(response):
    driver = config.get_driver()

    comment_post = driver.find_element(By.XPATH, "//button[@data-testid='reply']")
    comment_post.click()

    time.sleep(1)
    write_comment = driver.find_element(By.XPATH, "//div[@data-testid='tweetTextarea_0' and @role='textbox']")
    write_comment.send_keys(response)

    submit_comment = driver.find_element(By.XPATH, "//button[@data-testid='tweetButton' and @type='button']")
    submit_comment.click()

# comment_post(response="let's connect, just followed")

# comment_post(="lets connect, just followed")