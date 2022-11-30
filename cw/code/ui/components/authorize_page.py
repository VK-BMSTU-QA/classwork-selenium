from ui.locators import locators
from ui.components.base_component import BaseComponent
from ui.paths import paths


class AuthorizePage(BaseComponent):
    locators = locators.AuthorizeLocators
    PATH = paths.AUTHORIZE
