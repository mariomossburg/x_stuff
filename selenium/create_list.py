from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import config



# https://www.youtube.com/watch?v=gpCnquo-HvQ

def create_list():

    driver = config.get_driver()

    list_name = "selenium automated list"
    list_description = "an automated group creation with selenium"
    url = "https://x.com/home"

    driver.get(url)
    driver.maximize_window()


    try:
        wait = WebDriverWait(driver,2)
        click_menu = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@data-testid='AppTabBar_More_Menu']")
            )
        )
        click_menu.click()
    except:
        print("element not found clicking menu")


    try: 
        time.sleep(1)
        click_list = driver.find_element(By.XPATH, f"//a[@href='/{config.username}/lists' and @role='link']")
      
        click_list.click()
    except:
        print("no element found clicking list")



    try:
        time.sleep(1)
        create_new_list = driver.find_element(By.XPATH, "//a[@href='/i/lists/create' and @aria-label='Create a new List']")
        create_new_list.click()

        type_list_name = driver.find_element(By.XPATH, "//label[contains(@class, 'css-175oi2r')]//input[@name='name']")
        type_list_name.send_keys(list_name)

        type_list_description = driver.find_element(By.XPATH, "//textarea[@name='description']")
        type_list_description.send_keys(list_description)

        make_group_private = driver.find_element(By.XPATH, "//input[@type='checkbox' and @aria-describedby='CHECKBOX_1_LABEL']")
        make_group_private.click()


        click_next = driver.find_element(By.XPATH, "//button[@aria-label='Next' and @role='button' and @type='button']")
        click_next.click()

        # click_done = driver.find_element(By.XPATH, "//button[@aria-label='Close' and @role='button' and @type='button']")
        # click_done.click()

        wait = WebDriverWait(driver,2)
        click_done = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[text()='Done']")
            )
        )
        click_done.click()

    except:
        print("error making new list")

create_list()
