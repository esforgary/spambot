from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

def yandex_reg(phone):
    url = "https://passport.yandex.ru/auth?origin=dzen&retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fpush%3Fuuid%3Debe2dd9b-728c-4e29-8219-b2d127e01d4a%26retpath%3Dhttps%253A%252F%252Fdzen.ru%252Fapi%252Fauth%252Fweb%252Flogin-yandex%253Fretpath%253Dhttps%25253A%25252F%25252Fdzen.ru%25253Fauth%25253Dlogin%252526yredirect%25253Dtrue&backpath=https%3A%2F%2Fdzen.ru"

    options = webdriver.ChromeOptions()
    options.add_argument("Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36")

    chrome_driver_path = r"C:\Users\stass\PycharmProjects\SpamBot\driver\chromedriver.exe"
    os.environ["PATH"] += os.pathsep + chrome_driver_path
    driver = webdriver.Chrome()

    try:
        driver.get(url=url)
        time.sleep(4)

        phone_button = driver.find_element(By.CSS_SELECTOR, 'button[data-type="phone"]')
        phone_button.click()

        phone_input = driver.find_element(By.ID, "passp-field-phone")
        phone_input.clear()
        phone_input.send_keys(phone)
        time.sleep(3)

        login_button = driver.find_element(By.CLASS_NAME, 'Button2_type_submit')
        login_button.click()
        time.sleep(3)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

# yandex_reg("+79900447686")