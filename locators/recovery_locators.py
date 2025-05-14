
from selenium.webdriver.common.by import By

class RecoveryPageLocators:
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_NEW_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    SHOW_PASSWORD_BUTTON = (By.CSS_SELECTOR, "div.input__icon")
    PASSWORD_CONTAINER = (By.XPATH, "//input[@name='Введите новый пароль']/ancestor::div[contains(@class, 'input__container')]")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BTN = (By.XPATH, "//button[contains(text(), 'Войти')]")
    RECOVER_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")