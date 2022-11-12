import pytest
import time

from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.locators.profile_locators import ProfilePageLocators
from ui.base import BaseCase

class TestLogin(BaseCase):

    def test_lk1(self):
        time.sleep(5)

    def test_lk2(self):
        time.sleep(5)


class TestProfileNotification(BaseCase):
    authorize = True
    url = 'https://target-sandbox.my.com/profile/notifications'
    profile_locators = ProfilePageLocators()

    def test_change_notifications(self):
        self.driver.get(self.url)
        self.base_page.is_opened(self.url)
        
        elements = self.base_page.find_all(self.profile_locators.NOTIFICATIONS,15)
        expected = list(map( lambda elem: elem.is_selected(), elements))
        
        for index in range(len(elements)):
            expected[index] = not expected[index]
            self.base_page.elem_click(elements[index], 15)

        self.base_page.click(self.profile_locators.SAVE_NOTIFICATIONS, 15)

        time.sleep(3)

        result = list(map( lambda elem: elem.is_selected(), elements))
        assert expected == result

class TestProfileContacts(BaseCase):
    authorize = True
    url = 'https://target-sandbox.my.com/profile/contacts'
    profile_locators = ProfilePageLocators()
    
    def test_change_personal_data(self):
        self.driver.get(self.url)
        self.base_page.is_opened(self.url)

        input_field = self.base_page.find(self.profile_locators.CONTACT_INPUT_FIELD, 15)
        input_field.clear()

        expected = 'test_sd1fw'

        input_field.send_keys(expected)

        self.base_page.click(self.profile_locators.SAVE_CONTACTS, 15)

        time.sleep(3)

        input_field = self.base_page.find(self.profile_locators.CONTACT_INPUT_FIELD, 15)
        assert input_field.get_attribute('value') == expected

class TestHeaderButtons(BaseCase):
    authorize = True

    @pytest.mark.parametrize("button_locator, expected_url", [
        (
            BasePage.locators.BUTTON_TOOLS, 
            'https://target-sandbox.my.com/tools'
        ),
        (
            BasePage.locators.BUTTON_PROFILE, 
            'https://target-sandbox.my.com/profile'
        ),
        (
            BasePage.locators.BUTTON_BILLING, 
            'https://target-sandbox.my.com/billing'
        ),
        ])
    
    def test_page_switching(self, button_locator,expected_url):
        self.base_page.click(button_locator, 10)
        assert str(self.driver.current_url) == expected_url