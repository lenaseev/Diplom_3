
import allure
from pages.recovery_page import RecoveryPage
from urls import Urls

@allure.feature("Восстановление пароля")
class TestPasswordRecovery:
    @allure.title("Тест на ввод почты и клик по кнопке «Восстановить»")
    def test_password_recovery_flow(self, driver):
        recovery_page = RecoveryPage(driver)

        recovery_page.open(Urls.LOGIN_PAGE)
        recovery_page.click_recover_password()

        recovery_page.enter_email("test@yandex.ru")
        recovery_page.click_recover_button()

        assert recovery_page.get_current_url() == Urls.FORGOT_PASSWORD, "Не перешли на главную страницу"

    @allure.title("Тест перехода на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_navigate_to_recovery_page(self, driver):
        recovery_page = RecoveryPage(driver)

        recovery_page.open(Urls.LOGIN_PAGE)
        recovery_page.click_recover_password()
        assert "forgot-password" in recovery_page.get_current_url(), "Не перешли на страницу восстановления пароля"

    @allure.title("Тест переключения видимости пароля")
    def test_password_visibility_toggle(self, driver):
        recovery_page = RecoveryPage(driver)
        recovery_page.open(Urls.FORGOT_PASSWORD)

        recovery_page.enter_email("test@yandex.ru")
        recovery_page.click_recover_button()

        initial_state = recovery_page.get_password_field_state()
        assert initial_state['type'] == 'password', \
            f"Пароль должен быть скрыт по умолчанию. Текущее состояние: {initial_state}"

        recovery_page.toggle_password_visibility()
        new_state = recovery_page.get_password_field_state()
        assert new_state['type'] == 'text', \
            f"Пароль должен быть видимым после клика. Текущее состояние: {new_state}"

