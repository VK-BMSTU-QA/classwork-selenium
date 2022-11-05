from ui.pages.base_page import BasePage
from ui.login_setup.base_case import BaseCase

# тест подписок
class TestNotification(BaseCase):
    authorize = True
    url = 'https://target-sandbox.my.com/profile/notifications'
    def test_change_notifications_themes(self):
        self.driver.get(self.url)
        self.base_page.is_opened(self.url,15)
        # get_elementS 
        # in range elementS
        # запомнить их значения
        # 
        pass



    # тест в котором 
    # 1. логин пользователя
    # 2. переход в подписки
    # 3. чек подписок -- записать инфу в массив
    # 4. изменение подписки -- изменить 3 рандомные подписки
    # 5. сохранить изменения
    # 6. заассертить изменения




# тест инфы профиля