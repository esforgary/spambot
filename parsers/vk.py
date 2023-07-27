from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

def vk_reg(phone):
    url = "https://vk.com/"

    options = webdriver.ChromeOptions()
    options.add_argument("Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36")

    chrome_driver_path = r"C:\Users\stass\PycharmProjects\SpamBot\driver\chromedriver.exe"
    os.environ["PATH"] += os.pathsep + chrome_driver_path
    driver = webdriver.Chrome()

    try:
        driver.get(url=url)
        time.sleep(4)

        phone_input = driver.find_element(By.ID, "index_email")
        phone_input.clear()
        phone_input.send_keys(phone)
        time.sleep(3)

        login_button = driver.find_element(By.CLASS_NAME, 'VkIdForm__signInButton')
        login_button.click()
        time.sleep(6)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

# vk_reg("+79900447686")