import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.personal_account_locators import PersonalAccountLocators
from pages.base_page import BasePage
from urls import Urls

class PersonalAccountPage(BasePage):
    @allure.step("Открытие профиля пользователя")
    def open_profile(self):
        self.click(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON)
        self.wait_for_element_to_be_visible(PersonalAccountLocators.PROFILE_SECTION)


    @allure.step("Переход в раздел 'История заказов'")
    def open_order_history(self):
        self.click(PersonalAccountLocators.HISTORY_LINK)
        self.wait.until(EC.url_contains("order-history"))


    @allure.step("Выход из аккаунта")
    def logout(self):
        self.click(PersonalAccountLocators.LOGOUT_BUTTON)
        self.wait.until(EC.url_to_be(Urls.LOGIN_PAGE))


    @allure.step("Проверка отображения профиля")
    def is_profile_visible(self):
        return self.is_element_visible(PersonalAccountLocators.PROFILE_SECTION)

    @allure.step("Проверка отображения ссылки 'История заказов'")
    def is_order_history_visible(self):
        return self.is_element_visible(PersonalAccountLocators.HISTORY_LINK)


