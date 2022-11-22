from ui.pages.base_page import BasePage
from ui.base_case.base_case import BaseCase
from ui.pages.login_page import LoginPage


class TestLogin(BaseCase):
    authorize = False

    def test_login(self, credentials):
        login_page = LoginPage(self.driver)
        login_page.login(*credentials)
        assert str(
            self.driver.current_url) == 'https://target-sandbox.my.com/dashboard'
        assert self.base_page.find(BasePage.locators.USERNAME, self.base_page.default_timeout).get_attribute(
            'title') == credentials[0]
