
import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage
from urls import Urls

@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("Проверка открытия модального окна заказа")
    def test_order_modal_opens(self, authorized_driver):
        page = OrderFeedPage(authorized_driver).open()
        page.click_first_order()
        assert page.is_order_modal_visible(), "Модальное окно не открылось при клике на заказ"

    @allure.title("Проверка увеличения общего количества заказов")
    def test_done_total_increments(self, authorized_driver):
        order_feed = OrderFeedPage(authorized_driver).open()
        before = order_feed.get_total_orders_count()

        main_page = MainPage(authorized_driver)
        main_page.open(Urls.BASE_URL)
        main_page.add_ingredient_to_order()
        main_page.place_order()
        main_page.open(Urls.ORDER_FEED)
        after = OrderFeedPage(authorized_driver).get_total_orders_count()

        assert after > before, f"Счётчик 'выполнено за все время' не увеличился (было: {before}, стало: {after})"

    @allure.title("Проверка увеличения количества заказов за сегодня")
    def test_today_total_increments(self, authorized_driver):
        order_feed = OrderFeedPage(authorized_driver).open()
        before = order_feed.get_today_orders_count()

        main_page = MainPage(authorized_driver)
        main_page.open(Urls.BASE_URL)
        main_page.add_ingredient_to_order()
        main_page.place_order()
        main_page.open(Urls.ORDER_FEED)
        after = OrderFeedPage(authorized_driver).get_today_orders_count()

        assert after > before, f"Счётчик 'выполнено за сегодня' не увеличился (было: {before}, стало: {after})"

    @allure.title("Создание и проверка заказа")
    def test_create_and_verify_order(self, authorized_driver):
        # Инициализация страниц
        main_page = MainPage(authorized_driver).open(Urls.BASE_URL)
        order_feed = OrderFeedPage(authorized_driver)
        personal_acc_page = PersonalAccountPage(authorized_driver)

        main_page.add_ingredient_to_order()
        main_page.place_order()
        # Получаем номер заказа из модального окна
        created_order_number = main_page.get_order_number_from_modal()
        # Дополняем номер заказа нулями до 7 символов
        created_order_number = created_order_number.zfill(7)
        main_page.close_modal()
        main_page.open_profile()
        personal_acc_page.open_order_history()
        order_in_history = order_feed.get_history_order_number()
        order_in_feed = order_feed.get_history_order_number()
        assert created_order_number == order_in_feed, (
            f"Номера заказов не совпадают: {order_in_history} != {order_in_feed}"
        )

    @allure.title("Проверка появления заказа в разделе 'В работе'")
    def test_order_appears_in_progress_section(self, authorized_driver):
        # Открытие главной страницы
        main_page = MainPage(authorized_driver).open(Urls.BASE_URL)
        main_page.add_ingredient_to_order()
        main_page.place_order()
        # Получаем номер заказа из модального окна
        created_order_number = main_page.get_order_number_from_modal()
        # Дополняем номер заказа нулями до 7 символов
        created_order_number = created_order_number.zfill(7)
        main_page.close_modal()
        main_page = MainPage(authorized_driver).open(Urls.ORDER_FEED)
        # Получаем все номера заказов в разделе "В работе"
        in_progress_orders = main_page.get_orders_in_progress_numbers()
        assert created_order_number in in_progress_orders, (
            f"Ожидался заказ №{created_order_number} в разделе 'В работе', "
            f"но его нет среди: {in_progress_orders}"
        )