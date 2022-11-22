from ui.locators import locators
from ui.pages.base_page import BasePage


class ProfilePage(BasePage):
    locators = locators.ProfilePageLocators()

    def get_notification_themes_values(self, notification_themes_elems):
        return list(map(lambda elem: elem.is_selected(), notification_themes_elems))
