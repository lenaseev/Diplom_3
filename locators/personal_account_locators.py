from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    PROFILE_SECTION = (By.XPATH, "//a[text()='Профиль']")
    HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
