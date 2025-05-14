from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class MainPage(BasePage):
    # Навигация
    @allure.step("Клик по кнопке 'Конструктор'")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_LINK)
        return self

    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_LINK)
        return self

    @allure.step("Открытие профиля")
    def open_profile(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.PROFILE_SECTION))
        return self

    # Работа с ингредиентами
    @allure.step("Получение названий всех ингредиентов")
    def get_ingredient_names(self):
        elements = self.wait.until(
            EC.presence_of_all_elements_located(MainPageLocators.INGREDIENT_SECTION),
            message="Не удалось найти ингредиенты"
        )
        return [el.text for el in elements]

    @allure.step("Добавление ингредиента в заказ")
    def add_ingredient_to_order(self):
        self.drag_and_drop(
            MainPageLocators.INGREDIENT_ITEM,
            MainPageLocators.ORDER_ZONE
        )
        return self

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
        return self

    @allure.step("Клик по блоку деталей ингредиента")
    def click_ingredient_details(self):
        self.click(MainPageLocators.INGREDIENT_DETAILS)
        return self

    # Модальное окно ингредиента/заказа
    @allure.step("Проверка отображения модального окна")
    def is_modal_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_MODAL)

    @allure.step("Закрытие модального окна")
    def close_modal(self):
        # Ждём исчезновения анимации загрузки, если она была
        self.wait.until(EC.invisibility_of_element_located(MainPageLocators.MODAL_LOADING_ANIMATION))

        # Ждём кликабельности кнопки и нажимаем
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.CLOSE_MODAL_BUTTON)).click()

    @allure.step("Закрытие модального окна ингредиента")
    def close_modal_ingredients(self):
        # Ждём кликабельности кнопки и нажимаем
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.MODAL_CLOSE_INGREDIENTS)).click()


    # Оформление заказа
    @allure.step("Нажатие кнопки 'Оформить заказ'")
    def place_order(self):
        self.click(MainPageLocators.PLACE_ORDER_BUTTON)
        return self

    @allure.step("Ожидание обработки заказа (отображение номера)")
    def wait_for_order_processed(self, timeout=10):
        self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_NUMBER),
            message=f"Модальное окно заказа не появилось за {timeout} секунд"
        )
        return self

    @allure.step("Получение номера заказа")
    def get_order_number(self):
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_NUMBER))
        return self.get_element_text(MainPageLocators.ORDER_NUMBER)

    @allure.step("Получение номера созданного заказа из модального окна")
    def get_created_order_number(self):
        element = self.wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_MODAL))
        return element.text.strip().lstrip("#")

    @allure.step("Получение номера заказа из модального окна")
    def get_order_number_from_modal(self):
        # Ждём, пока появится номер заказа
        order_number_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_NUMBER_MODAL)
        )

        # Ждём, пока пропадёт анимация загрузки
        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located(MainPageLocators.MODAL_LOADING_ANIMATION)
        )


        order_number = order_number_element.text.strip()
        print(f"Полученный номер заказа из модального окна: {order_number}")
        return order_number

    @allure.step("Форматирование номера заказа '{number}'")
    def format_order_number(self, number):
        return number.strip().zfill(7)

    @allure.step("Получение номеров заказов в разделе 'В работе'")
    def get_orders_in_progress_numbers(self):
        elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, MainPageLocators.IN_PROGRESS_ORDER))
        )
        return [el.text.strip() for el in elements if el.text.strip()]

