import search_click_tweet_by_query
import time
import config
import follow_check
from selenium.webdriver.common.by import By
# import click_post
# import like
# import comment_post
# import follow_from_post
# import search_group
# import search



def main():
    comment = "let's connect, just followed you"

    driver = config.get_driver()
    time.sleep(1)
    tweet_element = search_click_tweet_by_query.search_tweet("connect")

    if tweet_element:
        time.sleep(1)

        if not follow_check.follow_button_check():
            time.sleep(1)

            like_post = driver.find_element(By.XPATH, "//button[@data-testid='like']")
            like_post.click()

            time.sleep(2)
            write_post =  driver.find_element(By.XPATH, "//div[@data-testid='tweetTextarea_0' and @role='textbox']")
            write_post.click()
            write_post.send_keys(comment)
            time.sleep(2)

            submit_post = driver.find_element(By.XPATH, "//button[@data-testid='tweetButton' and @type='button']")
            submit_post.click()

            # click_post.click_post(tweet_element)
            # time.sleep(3)
            # like.like_post()
            # comment_post.comment_post("lets connect, just followed you")                
        else:
            print("an error in second if")
    else:
        print("error for first if")
    
 
    

    


if __name__ == "__main__":
    main()