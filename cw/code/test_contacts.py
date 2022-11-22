from ui.base_case.base_case import BaseCase


class TestContacts(BaseCase):
    authorize = True
    url = 'https://target-sandbox.my.com/profile/contacts'

    def test_change_inn(self):
        self.driver.get(self.url)
        self.base_page.is_opened(self.url, self.base_page.default_timeout)
        inn_elem = self.base_page.find(
            self.profile_page.locators.CONTACT_INN, self.base_page.default_timeout)

        expected_inn_val = '1234567899'
        if inn_elem.get_attribute('value') == expected_inn_val:
            expected_inn_val = '1234567890'

        self.base_page.send_keys(inn_elem, expected_inn_val)

        self.base_page.click(
            self.profile_page.locators.SAVE_CONTANTS, self.base_page.default_timeout)

        self.base_page.wait_visability_of_elem(
            self.profile_page.locators.SUCCESS_SAVE_CONTACTS, self.base_page.default_timeout)

        upd_inn_elem = self.base_page.find(
            self.profile_page.locators.CONTACT_INN, self.base_page.default_timeout)
        assert upd_inn_elem.get_attribute('value') == expected_inn_val
