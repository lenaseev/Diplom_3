
import allure
from pages.personal_account_page import PersonalAccountPage
from urls import Urls

@allure.feature("Личный кабинет")
class TestPersonalAccount:

    @allure.title("Тест перехода в раздел профиля")
    def test_account_navigation(self, authorized_driver):
        account_page = PersonalAccountPage(authorized_driver)
        account_page.open_profile()

        assert account_page.is_profile_visible(), "Раздел профиля не отображается"
        assert "account/profile" in authorized_driver.current_url, "Не открылся раздел профиля"

    @allure.title("Тест перехода в историю заказов")
    def test_order_history_navigation(self, authorized_driver):
        account_page = PersonalAccountPage(authorized_driver)
        account_page.open_profile()
        account_page.open_order_history()

        assert "order-history" in authorized_driver.current_url, "Не открылась история заказов"
        assert account_page.is_order_history_visible(), "История заказов не отображается"

    @allure.title("Тест выхода из личного кабинета")
    def test_logout(self, authorized_driver):
        account_page = PersonalAccountPage(authorized_driver)
        account_page.open_profile()
        account_page.logout()

        assert Urls.LOGIN_PAGE in authorized_driver.current_url, "Не произошел выход из аккаунта"