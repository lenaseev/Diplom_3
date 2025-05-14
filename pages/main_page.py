from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure


class MainPage(BasePage):
    # Навигация
    @allure.step("Клик по кнопке 'Конструктор'")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_LINK)

    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_LINK)

    @allure.step("Открытие профиля")
    def open_profile(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.wait_for_element_to_be_visible(MainPageLocators.PROFILE_SECTION)

    # Работа с ингредиентами
    @allure.step("Получение названий всех ингредиентов")
    def get_ingredient_names(self):
        elements = self.find_elements(MainPageLocators.INGREDIENT_SECTION)
        return [el.text for el in elements]

    @allure.step("Добавление ингредиента в заказ")
    def add_ingredient_to_order(self):
        self.drag_and_drop(
            MainPageLocators.INGREDIENT_ITEM,
            MainPageLocators.ORDER_ZONE
        )


    @allure.step("Получение значения счётчика для ингредиента '{ingredient_name}'")
    def get_ingredient_counter(self, ingredient_name):
        elements = self.driver.find_elements(*MainPageLocators.INGREDIENT_ITEM)
        for el in elements:
            name = el.find_element(*MainPageLocators.INGREDIENT_NAME)
            if name.text.strip() == ingredient_name:
                try:
                    counter = el.find_element(*MainPageLocators.INGREDIENT_COUNTER)
                    if counter.is_displayed():
                        return int(counter.text)
                except:
                    return 0
        raise Exception(f"Ингредиент '{ingredient_name}' не найден")

    @allure.step("Получение значения счётчика (если > 0)")
    def get_counter_value(self):
        try:
            WebDriverWait(self.driver, 5).until(
                lambda d: any(int(el.text) > 0 for el in d.find_elements(*MainPageLocators.INGREDIENT_COUNTER))
            )
            counters = self.driver.find_elements(*MainPageLocators.INGREDIENT_COUNTER)
            for counter in counters:
                if counter.is_displayed() and counter.text.isdigit():
                    value = int(counter.text)
                    if value > 0:
                        return value
            return 0
        except Exception as e:
            print(f"Ошибка при получении счётчика: {e}")
            return 0

    @allure.step("Открытие деталей ингредиента по имени '{name}'")
    def open_ingredient_details(self, name):
        locator = (MainPageLocators.INGREDIENT_ITEM[0],
                   f"{MainPageLocators.INGREDIENT_ITEM[1]}[contains(text(), '{name}')]")
        self.click(locator)


    @allure.step("Клик по блоку деталей ингредиента")
    def click_ingredient_details(self):
        self.click(MainPageLocators.INGREDIENT_DETAILS)


    # Модальное окно ингредиента/заказа
    @allure.step("Проверка отображения модального окна")
    def is_modal_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_MODAL)

    @allure.step("Проверка, что блок ингредиентов отображается")
    def is_ingredient_block_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_SECTION)

    @allure.step("Закрытие модального окна")
    def close_modal(self):
        # Ждём исчезновения анимации загрузки, если она была
        self.wait_for_element_to_disappear(MainPageLocators.MODAL_LOADING_ANIMATION)
        self.click(MainPageLocators.CLOSE_MODAL_BUTTON)

    @allure.step("Закрытие модального окна ингредиента")
    def close_modal_ingredients(self):
        # Ждём кликабельности кнопки и нажимаем
        self.click(MainPageLocators.MODAL_CLOSE_INGREDIENTS)

    # Оформление заказа
    @allure.step("Нажатие кнопки 'Оформить заказ'")
    def place_order(self):
        self.click(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step("Ожидание обработки заказа (отображение номера)")
    def wait_for_order_processed(self, timeout=10):
        self.wait_for_element_to_be_visible(MainPageLocators.ORDER_NUMBER)


    @allure.step("Получение номера заказа")
    def get_order_number(self):
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_NUMBER))
        return self.get_element_text(MainPageLocators.ORDER_NUMBER)

    @allure.step("Получение номера созданного заказа из модального окна")
    def get_created_order_number(self):
        return self.get_element_text(MainPageLocators.ORDER_NUMBER)

    @allure.step("Получение номера заказа из модального окна")
    def get_order_number_from_modal(self):
        order_number_element = self.wait_for_custom_condition(
            EC.visibility_of_element_located(MainPageLocators.ORDER_NUMBER_MODAL), timeout=20
        )
        self.wait_for_custom_condition(
            EC.invisibility_of_element_located(MainPageLocators.MODAL_LOADING_ANIMATION), timeout=20
        )

        order_number = order_number_element.text.strip()
        print(f"Полученный номер заказа из модального окна: {order_number}")
        return order_number

    @allure.step("Форматирование номера заказа '{number}'")
    def format_order_number(self, number):
        return number.strip().zfill(7)

