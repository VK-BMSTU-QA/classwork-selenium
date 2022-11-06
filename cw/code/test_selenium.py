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

    element = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[1]")
    element.click()

    element1 = driver.find_element(By.NAME, "email")
    element1.clear()
    element1.send_keys(email)

    element2 = driver.find_element(By.NAME, "password")
    element2.clear()
    element2.send_keys(password)

    element3 = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div/div[4]/div[1]")
    element3.click()


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

        element4 = driver.find_element(
            By.XPATH,
            '//a[@href="/billing"]'
        )
        element4.click()

        time.sleep(10)

        element51 = driver.find_element(
            By.XPATH,
            '//a[@href="/profile"]'
        )
        element51.click()

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
        element5 = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li[2]/div[1]/div/div/"
            "input"
        )
        element5.clear()
        element5.send_keys("Голубев Сергей Николаевич")

        time.sleep(2)

        element6 = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/button"
        )
        element6.click()

    def tearDown(self):
        self.driver.close()


class ChangingSubscriptions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_check_header(self):
        driver = self.driver
        authorize(driver)

        driver.get("https://target-sandbox.my.com/profile/notifications")
        time.sleep(5)

        element7 = driver.find_element(By.ID, "notifications-event")
        element7.click()

        time.sleep(2)

        element8 = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[8]/button"
        )
        element8.click()


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

