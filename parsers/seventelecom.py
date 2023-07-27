from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

def seventelecom_reg(phone):
    url = "https://lk.7telecom.ru/auth"

    options = webdriver.ChromeOptions()
    options.add_argument("Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36")

    chrome_driver_path = r"C:\Users\stass\PycharmProjects\SpamBot\driver\chromedriver.exe"
    os.environ["PATH"] += os.pathsep + chrome_driver_path
    driver = webdriver.Chrome()

    try:
        driver.get(url=url)
        time.sleep(4)

        phone_input = driver.find_element(By.CLASS_NAME, "MuiOutlinedInput-inputAdornedStart")
        phone_input.clear()
        phone_input.send_keys(phone)
        time.sleep(3)

        choose_phone_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div[1]/div/form/button[2]')
        choose_phone_button.click()

        time.sleep(3)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

# seventelecom_reg("9900447686")