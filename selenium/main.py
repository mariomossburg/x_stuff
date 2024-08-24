from selenium.webdriver.common.by import By
import search_click_tweet_by_query
import time
import config
import click_post
# import follow_check
import like_post
# import comment_post
# import follow_from_post
# import search_group
# import search



def main():
    driver = config.get_driver()
    driver.maximize_window()
    time.sleep(1)

    # Try this
    # click_post.click_post()
    
    # Or this
    like_post.like_post()
    


if __name__ == "__main__":
    main()