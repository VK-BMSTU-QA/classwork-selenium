from selenium.webdriver.common.by import By

class BasePageLocators:
    QUERY_LOCATOR = (By.NAME, 'q')
    QUERY_LOCATOR_ID = (By.ID, 'id-search-field')
    GO_BUTTON_LOCATOR = (By.XPATH, '//*[@id="submit"]')
    START_SHELL = (By.ID, 'start-shell')
    PYTHON_CONSOLE = (By.ID, 'hterm:row-nodes')
    LOGIN_BUTTON = (By.CLASS_NAME, 'responseHead-module-button-2yl51i')
    
    BUTTON_PRO = (By.XPATH, '//a[@href="/pro"]')
    BUTTON_PROFILE = (By.XPATH, '//a[@href="/profile"]')
    BUTTON_SEGMENTS = (By.XPATH, '//a[@href="/segments"]')
    BUTTON_BILLING = (By.XPATH, '//a[@href="/billing"]')
    BUTTON_TOOLS = (By.XPATH, '//a[@href="/tools"]')
