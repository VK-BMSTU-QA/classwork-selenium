import pytest
from ui.paths import paths
from ui.components.changing_subscriptions_page import ChangingSubscriptionsPage
from ui.base_case.base_case import BaseCase
import time


class TestEditContact(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = ChangingSubscriptionsPage(driver, url_config)

    def test_edit_contact(self):
        self.page.authorize()
        self.page.click(self.page.locators.PROFILE_BUTTON)
        self.page.click(self.page.locators.FOLLOW_BUTTON)
        self.page.click(self.page.locators.CHANGE_MODERATION)
        self.page.click(self.page.locators.SAVE_BUTTON)
        time.sleep(20)

