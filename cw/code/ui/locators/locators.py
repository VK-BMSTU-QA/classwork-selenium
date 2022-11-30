from selenium.webdriver.common.by import By


class BasePageLocators:
    che = ()


class AuthorizeLocators:
    LOGIN_BUTTON = (By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[1]')
    LOGIN_BUTTON2 = (By.CLASS_NAME, 'authForm-module-button-1u2DYF')
    INPUT_EMAIL = (By.XPATH, '/html/body/div[2]/div/div[2]/div/form/div/div[1]/input')
    INPUT_PASSWORD = (By.XPATH, '/html/body/div[2]/div/div[2]/div/form/div/div[2]/input')


class HeaderLocators:
    BILLING_BUTTON = (By.XPATH, '//a[@href="/billing"]')
    PROFILE_BUTTON = (By.XPATH, '//a[@href="/profile"]')


class ContactLocators:
    PROFILE_BUTTON = (By.XPATH, '//a[@href="/profile"]')
    FIO_INPUT = (
            By.XPATH,
            "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li[2]/div[1]/div/div/"
            "input"
        )
    SAVE_BUTTON = (
        By.XPATH,
        "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/button"
    )


class ChangingSubscriptionsLocators:
    PROFILE_BUTTON = (By.XPATH, '//a[@href="/profile"]')
    FOLLOW_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/div/div[4]/a')
    CHANGE_MODERATION = (By.ID, "notifications-event")
    SAVE_BUTTON = (
        By.XPATH,
        "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[8]/button"
    )
