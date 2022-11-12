import time
from ui.pages.base_page import BasePage
from ui.locators.login_locators import LoginPageLocators
from ui.locators.basic_locators import BasePageLocators

class LoginPage(BasePage):
    basic_locators = BasePageLocators()
    login_locators = LoginPageLocators()

    def login(self, user, password):
        self.click(self.basic_locators.LOGIN_BUTTON)
        self.find(self.login_locators.LOGIN_INPUT).send_keys(user)
        self.find(self.login_locators.PASSWORD_INPUT).send_keys(password)

        self.click(self.login_locators.LOGIN_BUTTON)

        time.sleep(5)
