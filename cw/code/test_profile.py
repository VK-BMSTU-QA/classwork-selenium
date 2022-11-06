import random
from ui.login_setup.base_case import BaseCase


class TestNotification(BaseCase):
    authorize = True
    url = 'https://target-sandbox.my.com/profile/notifications'

    def test_change_notifications_themes(self):
        self.driver.get(self.url)
        self.base_page.is_opened(self.url, 15)
        checkbox_elems = self.base_page.find_all_elemets(
            self.profile_page.locators.NOTIFICATION_THEMES,15)
        expected_values_checkbox_elems = self.profile_page.get_notification_themes_values(
            checkbox_elems)

        pos_to_swicth = [0,3,9]

        for pos in pos_to_swicth:
            expected_values_checkbox_elems[pos] = not expected_values_checkbox_elems[pos]
            self.base_page.elem_click(checkbox_elems[pos], 15)

        self.base_page.click(
            self.profile_page.locators.SAVE_NOTIFICATION_THEMES, 15)

        self.base_page.wait_visability_of_elem(
            self.profile_page.locators.SUCCESS_SAVE_NOTIFICATION_THEMES, 15)

        values_checkbox_elems = self.profile_page.get_notification_themes_values(
            checkbox_elems)

        assert expected_values_checkbox_elems == values_checkbox_elems


class TestContacts(BaseCase):
    authorize = True
    url = 'https://target-sandbox.my.com/profile/contacts'
    
    def test_change_fio(self):
        self.driver.get(self.url)
        self.base_page.is_opened(self.url, 15)
        inn_elem = self.base_page.find(self.profile_page.locators.CONTACT_INN, 15)

        if inn_elem.get_attribute('value') != "":
            expected_inn_val = list(inn_elem.get_attribute('value'))
            expected_inn_val[0] = chr(
                (int(expected_inn_val[0])+1) % 10 + ord('0'))
            expected_inn_val=''.join(expected_inn_val)
        else:
            expected_inn_val = '1234567899'

        self.base_page.send_keys(inn_elem, expected_inn_val)

        self.base_page.click(
            self.profile_page.locators.SAVE_CONTANTS, 15)

        self.base_page.wait_visability_of_elem(
            self.profile_page.locators.SUCCESS_SAVE_CONTACTS, 15)

        upd_inn_elem = self.base_page.find(self.profile_page.locators.CONTACT_INN, 15)
        assert upd_inn_elem.get_attribute('value') == expected_inn_val
