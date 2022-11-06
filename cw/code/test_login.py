from ui.pages.base_page import BasePage
from ui.login_setup.base_case import BaseCase
from ui.pages.login_page import LoginPage

class TestLogin(BaseCase):
    authorize = False
    
    def test_login(self, credentials):
        login_page = LoginPage(self.driver)
        login_page.login(*credentials)
        assert str(self.driver.current_url) == 'https://target-sandbox.my.com/dashboard'
        assert self.base_page.find(BasePage.locators.USERNAME, 15).get_attribute('title') == credentials[0]
