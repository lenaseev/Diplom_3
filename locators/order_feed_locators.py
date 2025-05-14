
from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    PAGE_HEADER = (By.XPATH, "//h1[text()='Лента заказов']")
    HISTORY_PAGE_LINK = (By.XPATH, "//p[text()='История заказов']")
    # Номер заказа
    ORDER_NUMBER = (By.CSS_SELECTOR, "p.text_type_digits-default.mb-10")

    # Статистика
    TOTAL_ORDERS = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    TODAY_ORDERS = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
    ORDERS_LIST = (By.CSS_SELECTOR, "ul.OrderFeed_list__OLh59")

    # Локаторы для страницы История заказов (если нужны отдельные локаторы для истории заказов)
    HISTORY_PAGE_HEADER = (By.XPATH, "//h1[text()='История заказов']")
    HISTORY_ORDER_NUMBER = (By.CSS_SELECTOR, ".OrderHistory_link__1iNby p.text_type_digits-default")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    PROFILE_SECTION = (By.XPATH, "//a[text()='Профиль']")
    HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    CLOSE_MODAL_BUTTON = (By.CSS_SELECTOR, "button.Modal_modal__close__TnseK")
    ORDERS_IN_PROGRESS_NUMBERS = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul[1]/li")


