import allure
from locators.recovery_locators import RecoveryPageLocators
from pages.base_page import BasePage
from urls import Urls


class RecoveryPage(BasePage):
    @allure.step("Ввод email: {email}")
    def enter_email(self, email):
        self.input_text(RecoveryPageLocators.EMAIL_INPUT, email)


    @allure.step("Нажатие на кнопку восстановления")
    def click_recover_button(self):
        self.click(RecoveryPageLocators.RECOVER_BUTTON)


    @allure.step("Переключение видимости пароля")
    def toggle_password_visibility(self):
        self.click(RecoveryPageLocators.SHOW_PASSWORD_BUTTON)


    @allure.step("Получение состояния поля пароля")
    def get_password_field_state(self):
        container = self.wait_for_element_to_be_visible(RecoveryPageLocators.PASSWORD_CONTAINER)
        password_input = self.find_element(RecoveryPageLocators.PASSWORD_NEW_INPUT)

        return {
            'is_active': 'input_status_active' in container.get_attribute('class'),
            'type': password_input.get_attribute('type'),
            'is_visible': password_input.get_attribute('type') == 'text'
        }

    @allure.step("Переход по ссылке 'Восстановить пароль'")
    def click_recover_password(self):
        self.click(RecoveryPageLocators.RECOVER_PASSWORD_LINK)


    @allure.step("Ввод нового пароля")
    def enter_password(self, password):
        self.input_text(RecoveryPageLocators.PASSWORD_INPUT, password)

    @allure.step("Нажатие на кнопку входа")
    def click_login(self):
        self.click(RecoveryPageLocators.LOGIN_BTN)


    @allure.step("Проверка успешного входа")
    def is_login_successful(self):
        try:
            self.wait_for_url_to_be(Urls.BASE_URL)
            return True
        except:
            return False

    @allure.step("Переход по ссылке регистрации")
    def click_register_link(self):
        self.click(RecoveryPageLocators.REGISTER_LINK)

