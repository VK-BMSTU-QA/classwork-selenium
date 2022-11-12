from selenium.webdriver.common.by import By

class ProfilePageLocators:
    NOTIFICATIONS = (By.XPATH, '//input[@class="profile__list__row__box js-mailing-item" and @type="checkbox"]')
    SAVE_NOTIFICATIONS = (By.XPATH, '//div[@class="button__text" and text() = "Сохранить"]')
    SUCCESS_SAVE_NOTIFICATIONS = (By.XPATH, '//div[@class="_notification__content js-notification-content" and text() = "Информация успешно сохранена"]')
    
    CONTACT_INPUT_FIELD=(By.XPATH, '//div[@class="input" and @data-name = "ordInn"]/div/input')
    SAVE_CONTACTS = (By.XPATH, '//div[@class="button__text" and text() = "Сохранить"]')
    SUCCESS_SAVE_CONTACTS = (By.XPATH, '//div[@class="_notification__content js-notification-content" and text() = "Информация успешно сохранена"]')
