import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.personal_account_locators import PersonalAccountLocators
from pages.base_page import BasePage
from urls import Urls

class PersonalAccountPage(BasePage):
    @allure.step("Открытие профиля пользователя")
    def open_profile(self):
        self.click(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON)
        self.wait.until(EC.visibility_of_element_located(PersonalAccountLocators.PROFILE_SECTION))
        return self

    @allure.step("Переход в раздел 'История заказов'")
    def open_order_history(self):
        self.click(PersonalAccountLocators.HISTORY_LINK)
        self.wait.until(EC.url_contains("order-history"))
        return self

    @allure.step("Выход из аккаунта")
    def logout(self):
        self.click(PersonalAccountLocators.LOGOUT_BUTTON)
        self.wait.until(EC.url_to_be(Urls.LOGIN_PAGE))
        return self

    @allure.step("Проверка отображения профиля")
    def is_profile_visible(self):
        return self.is_element_visible(PersonalAccountLocators.PROFILE_SECTION)

    @allure.step("Проверка отображения ссылки 'История заказов'")
    def is_order_history_visible(self):
        return self.is_element_visible(PersonalAccountLocators.HISTORY_LINK)


