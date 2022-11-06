import unittest
import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from dotenv import load_dotenv

load_dotenv()

email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')


def authorize(my_driver):
    driver = my_driver
    driver.set_window_size(1920, 1080)
    driver.get("https://target-sandbox.my.com/")
    time.sleep(10)

    login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[1]")
    login_button.click()

    email_input = driver.find_element(By.NAME, "email")
    email_input.clear()
    email_input.send_keys(email)

    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys(password)

    yet_login_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div/div[4]/div[1]")
    yet_login_button.click()


class Authorize(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_authorize(self):
        driver = self.driver
        authorize(driver)

    def tearDown(self):
        self.driver.close()


class CheckHeader(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_check_header(self):
        driver = self.driver
        authorize(driver)

        time.sleep(10)

        billing = driver.find_element(
            By.XPATH,
            '//a[@href="/billing"]'
        )
        billing.click()

        time.sleep(10)

        profile = driver.find_element(
            By.XPATH,
            '//a[@href="/profile"]'
        )
        profile.click()

    def tearDown(self):
        self.driver.close()


class EditContact(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_authorize(self):
        driver = self.driver
        authorize(driver)

        driver.get("https://target-sandbox.my.com/profile/contacts")
        time.sleep(5)
        FIO_input = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li[2]/div[1]/div/div/"
            "input"
        )
        FIO_input.clear()
        FIO_input.send_keys("Голубев Сергей Николаевич")

        time.sleep(2)

        save_button = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/button"
        )
        save_button.click()

    def tearDown(self):
        self.driver.close()


class ChangingSubscriptions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_changing_subscriptions(self):
        driver = self.driver
        authorize(driver)

        driver.get("https://target-sandbox.my.com/profile/notifications")
        time.sleep(5)

        change_moderation = driver.find_element(By.ID, "notifications-event")
        change_moderation.click()

        time.sleep(2)

        save_button = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[8]/button"
        )
        save_button.click()


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

