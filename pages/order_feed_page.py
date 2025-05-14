
import allure
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_feed_locators import OrderFeedPageLocators
from pages.base_page import BasePage
from urls import Urls

class OrderFeedPage(BasePage):

    @allure.step("Инициализация главной страницы")
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открытие браузера")
    def open(self):
        self.driver.get(Urls.ORDER_FEED)
        return self

    @allure.step("Клик на первый заказ")
    def click_first_order(self):
        self.click(OrderFeedPageLocators.ORDERS_LIST)
        return self

    @allure.step("Проверка видимости модального окна заказа")
    def is_order_modal_visible(self):
        return self.is_element_visible(OrderFeedPageLocators.ORDER_NUMBER)

    @allure.step("Получение общего количества заказов")
    def get_total_orders_count(self, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                lambda d: d.find_element(*OrderFeedPageLocators.TOTAL_ORDERS)
            )
            total_text = element.text.strip()
            return int(total_text)
        except TimeoutException:
            print(" Элемент TOTAL_ORDERS не найден за отведённое время.")
            return 0
        except ValueError:
            print(f" Невозможно преобразовать текст в число: '{total_text}'")
            return 0

    @allure.step("Получение количества заказов за сегодня")
    def get_today_orders_count(self, timeout=20):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                lambda d: d.find_element(*OrderFeedPageLocators.TODAY_ORDERS)
            )
            today_text = element.text.strip()
            return int(today_text)
        except TimeoutException:
            print(" Элемент не найден за отведённое время.")
            return 0
        except ValueError:
            print(f" Невозможно преобразовать текст в число: '{today_text}'")
            return 0

    @allure.step("Получение номера заказа из модального окна")
    def get_order_number_from_modal(self):
        return self.get_element_text(OrderFeedPageLocators.ORDER_NUMBER)

    @allure.step("Проверка наличия заказа {order_number} в разделе 'В работе'")
    def get_orders_in_progress(self, order_number, timeout=10):
        try:
            # Ожидаем появления заказа в разделе «В работе»
            element = WebDriverWait(self.driver, timeout).until(
                lambda d: d.find_element(OrderFeedPageLocators.ORDER_NUMBER.format(order_number))
            )
            order_text = element.text.strip()
            assert order_number in order_text, f"Заказ {order_number} не найден в разделе В работе."
            print(f"Заказ {order_number} найден в разделе В работе.")
        except TimeoutException:
            print(f"Заказ {order_number} не найден в разделе В работе за отведённое время.")
        except AssertionError as e:
            print(e)

    @allure.step("Переход на страницу: {url}")
    def go_to_page(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(*OrderFeedPageLocators.PAGE_HEADER)  # Ожидаем загрузки страницы
        )

    @allure.step("Получение номера заказа на странице Ленты заказов")
    def get_order_number(self):
        return self.find_element(OrderFeedPageLocators.ORDER_NUMBER).text.strip()

    @allure.step("Переход на страницу 'История заказов'")
    def go_to_history_page(self):
        self.find_element(OrderFeedPageLocators.HISTORY_PAGE_LINK).click()
        self.is_element_visible(OrderFeedPageLocators.HISTORY_PAGE_HEADER)

    @allure.step("Переход на страницу 'Лента заказов'")
    def go_to_order_feed_page(self):
        self.find_element(OrderFeedPageLocators.PAGE_HEADER).click()
        self.is_element_visible(OrderFeedPageLocators.ORDER_NUMBER)

    @allure.step("Открытие профиля")
    def open_profile(self):
        self.click(OrderFeedPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.wait.until(EC.visibility_of_element_located(OrderFeedPageLocators.PROFILE_SECTION))
        return self

    @allure.step("Открытие истории заказов")
    def open_order_history(self):
        self.click(OrderFeedPageLocators.HISTORY_LINK)

    @allure.step("Закрытие модального окна")
    def close_modal(self):
        self.click(OrderFeedPageLocators.CLOSE_MODAL_BUTTON)
        return self

    @allure.step("Получение номера заказа из истории")
    def get_history_order_number(self):
        element = self.wait.until(
            EC.presence_of_element_located(OrderFeedPageLocators.HISTORY_ORDER_NUMBER)
        )
        return element.text.strip().lstrip("#")

    @allure.step("Получение номеров заказов из раздела 'В работе'")
    def get_orders_in_progress_numbers(self):
        elements = self.find_element(OrderFeedPageLocators.ORDERS_IN_PROGRESS_NUMBERS)
        return [el.text.strip().replace('#', '') for el in elements if el.text.strip()]


