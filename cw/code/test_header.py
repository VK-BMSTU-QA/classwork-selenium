import pytest
from ui.pages.base_page import BasePage
from ui.login_setup.base_case import BaseCase

class TestHeaderFollowLinks(BaseCase):
    authorize = True

    @pytest.mark.parametrize("link_locator,expected_url", [
        (BasePage.locators.HEADER_TOOLS, 'https://target-sandbox.my.com/tools'),
        (BasePage.locators.HEADER_PROFILE, 'https://target-sandbox.my.com/profile'),
        (BasePage.locators.HEADER_BILLING, 'https://target-sandbox.my.com/billing'),
        ])
    def test_follow_links(self, link_locator,expected_url):
        self.base_page.click(link_locator, 10)
        assert str(self.driver.current_url) == expected_url