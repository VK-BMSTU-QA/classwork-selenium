from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_INPUT = (By.XPATH, '//input[@name = "email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name = "password"]')
    LOGIN_BUTTON = (By.CLASS_NAME, 'authForm-module-button-1u2DYF')
