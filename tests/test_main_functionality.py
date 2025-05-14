import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from urls import Urls

@allure.feature("Проверка основного функционала")
class TestMainFunctionality:

    @allure.title("Переход в конструктор с главной страницы")
    def test_constructor_navigation(self, driver):
        main_page = MainPage(driver)

        main_page.open(Urls.BASE_URL)
        main_page.click_constructor()

        assert driver.current_url == Urls.BASE_URL
        assert main_page.is_element_visible(MainPageLocators.INGREDIENT_SECTION)

    @allure.title("Переход в ленту заказов из неавторизованного состояния")
    def test_order_feed_navigation(self, driver):
        main_page = MainPage(driver)
        main_page.open(Urls.BASE_URL)
        main_page.click_order_feed()

        assert driver.current_url == Urls.ORDER_FEED

    @allure.title("Открытие модального окна ингредиента")
    def test_ingredient_modal_workflow(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        main_page.open(Urls.BASE_URL)
        main_page.click_ingredient_details()

        assert main_page.is_modal_visible(), "Модальное окно ингредиента не открылось"
        assert "ingredient" in authorized_driver.current_url

    @allure.title("Закрытие модального окна ингредиента")
    def test_close_modal_workflow(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        main_page.open(Urls.BASE_URL)
        main_page.click_ingredient_details()
        assert main_page.is_modal_visible(), "Модалка не открылась"
        main_page.close_modal_ingredients()
        assert not main_page.close_modal_ingredients(), "Модальное окно не закрылось"

    @allure.title("Создание заказа авторизованным пользователем")
    def test_successful_order_creation(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        main_page.open(Urls.BASE_URL)
        main_page.add_ingredient_to_order()
        main_page.place_order()

        assert main_page.is_modal_visible(), "Модальное окно заказа не появилось"

    @allure.title("Счётчик увеличивается при добавлении ингредиента")
    def test_ingredient_counter_increases(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        main_page.open(Urls.BASE_URL)
        main_page.add_ingredient_to_order()

        counter = main_page.get_counter_value()
        assert counter > 0, "Счетчик не увеличился после добавления ингредиента"
