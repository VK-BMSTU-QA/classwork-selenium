import pytest
from ui.paths import paths
from ui.components.header_elemet import HeaderPage
from ui.base_case.base_case import BaseCase


class TestHeader(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = HeaderPage(driver, url_config)

    def test_header(self):
        self.page.authorize()
        self.page.click(self.page.locators.BILLING_BUTTON)
        self.page.click(self.page.locators.PROFILE_BUTTON)
        assert self.page.is_url(paths.PROFILE)
