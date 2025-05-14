
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)
        return self

    def click(self, locator):
        """Кликает по элементу, ожидая его кликабельности"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        return self

    def input_text(self, locator, text):
        """Вводит текст в поле ввода, очищая его перед этим"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        return self

    def is_element_visible(self, locator):
        """Проверяет видимость элемента, возвращая True или False"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except:
            return False

    def get_element_text(self, locator):
        """Получает текст из элемента"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def drag_and_drop(self, source_locator, target_locator):
        """Перетаскивает элемент с одного места на другое"""
        source = self.wait.until(EC.visibility_of_element_located(source_locator))
        target = self.wait.until(EC.visibility_of_element_located(target_locator))
        ActionChains(self.driver).drag_and_drop(source, target).perform()
        return self

    def find_element(self, locator):
        """Находит первый элемент по локатору"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """Находит все элементы по локатору"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def get_current_url(self):
        """Возвращает текущий URL страницы"""
        try:
            return self.driver.current_url
        except Exception as e:
            print(f"Error retrieving current URL: {e}")
            return None