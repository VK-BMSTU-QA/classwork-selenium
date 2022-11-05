from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_BUTTON = (By.CLASS_NAME, 'responseHead-module-button-2yl51i')
    HEADER_DASHBOARD = (By.XPATH, '//a[@href="/dashboard"]')
    HEADER_STATISTICS = (By.XPATH, '//a[@href="//statistics"]')
    HEADER_PRO = (By.XPATH, '//a[@href="/pro"]')
    HEADER_PROFILE = (By.XPATH, '//a[@href="/profile"]')
    HEADER_SEGMENTS = (By.XPATH, '//a[@href="/segments"]')
    HEADER_BILLING = (By.XPATH, '//a[@href="/billing"]')
    HEADER_TOOLS = (By.XPATH, '//a[@href="/tools"]')
    HEADER_HELP = (By.XPATH, '//a[@href="//target.my.com/help/advertisers/ru"]')
    USERNAME = (By.CLASS_NAME,'right-module-userNameWrap-3Odw2D')


class LoginPageLocators(BasePageLocators):
    LOGIN_INPUT = (By.XPATH, '//input[@name = "email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name = "password"]')
    PASS_LOGIN_CREDS_BUTTON = (By.CLASS_NAME, 'authForm-module-button-1u2DYF')
