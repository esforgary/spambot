from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

def telegram_reg(phone):
    url = "https://web.telegram.org/a/"

    options = webdriver.ChromeOptions()
    options.add_argument("Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36")

    chrome_driver_path = r"C:\Users\stass\PycharmProjects\SpamBot\driver\chromedriver.exe"
    os.environ["PATH"] += os.pathsep + chrome_driver_path
    driver = webdriver.Chrome()

    try:
        driver.get(url=url)
        time.sleep(15)

        phone_input = driver.find_element(By.ID, "sign-in-phone-number")
        phone_input.clear()
        phone_input.send_keys(phone)
        time.sleep(3)

        login_button = driver.find_element(By.XPATH, '//*[@id="auth-phone-number-form"]/div/form/button[1]')
        login_button.click()
        time.sleep(3)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

# telegram_reg("+79900447686")