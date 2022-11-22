from ui.base_case.base_case import BaseCase


class TestNotification(BaseCase):
    authorize = True
    url = 'https://target-sandbox.my.com/profile/notifications'

    def test_change_notifications_themes(self):
        self.driver.get(self.url)
        self.base_page.is_opened(self.url, self.base_page.default_timeout)
        checkbox_elems = self.base_page.find_all_elemets(
            self.profile_page.locators.NOTIFICATION_THEMES, self.base_page.default_timeout)
        expected_values_checkbox_elems = self.profile_page.get_notification_themes_values(
            checkbox_elems)

        element_to_swicth = {"news": 0, "moderation": 3, "actions": 9}

        for name in element_to_swicth:
            expected_values_checkbox_elems[element_to_swicth[name]
                                           ] = not expected_values_checkbox_elems[element_to_swicth[name]]
            self.base_page.elem_click(
                checkbox_elems[element_to_swicth[name]], self.base_page.default_timeout)

        self.base_page.click(
            self.profile_page.locators.SAVE_NOTIFICATION_THEMES, self.base_page.default_timeout)

        self.base_page.wait_visability_of_elem(
            self.profile_page.locators.SUCCESS_SAVE_NOTIFICATION_THEMES, self.base_page.default_timeout)

        values_checkbox_elems = self.profile_page.get_notification_themes_values(
            checkbox_elems)

        assert expected_values_checkbox_elems == values_checkbox_elems
