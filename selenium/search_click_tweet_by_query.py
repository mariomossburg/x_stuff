from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import config
import time 

# import click_post



def search_tweet(queries):
    driver = config.get_driver()

    time.sleep(1)
    tweets = driver.find_elements(By.XPATH, '//div[@data-testid="tweetText"]')

    for index,tweet in enumerate(tweets):
            spans = tweet.find_elements(By.XPATH, ".//span")
            full_tweet_text = ' '.join(span.text for span in spans).strip().lower()

            print(f"tweet '{index}': '{full_tweet_text}'")

            if queries in full_tweet_text:
                print(f"Keyword {queries} found in tweet {index}")

                tweet.click()
                print("tweet clicked successsfully")
                return tweet, 
    return None, None
                # click_tweet  = tweet.find_element(By.XPATH, ".//ancestor::article")
                # click_tweet.click()
                # print(f"Tweet {index} clicked")
                # break
        # is not working
            # if index >= 30:
            #     break


# search_tweet(queries = 'connect')