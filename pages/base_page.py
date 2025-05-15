
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

    def get_current_url(self):
        return self.driver.current_url

    def click(self, locator):
        """Кликает по элементу, ожидая его кликабельности"""
        element = self.wait_for_element_to_be_clickable(locator)
        element.click()
    def input_text(self, locator, text):
        """Вводит текст в поле ввода, очищая его перед этим"""
        element = self.wait_for_element_to_be_visible(locator)
        element.clear()
        element.send_keys(text)
        return self

    def is_element_visible(self, locator):
        """Проверяет видимость элемента, возвращая True или False"""
        try:
            element = self.wait_for_element_to_be_visible(locator)
            return element.is_displayed()
        except:
            return False

    def get_element_text(self, locator):
        """Получает текст из элемента"""
        element = self.wait_for_element_to_be_visible(locator)
        return element.text

    def drag_and_drop(self, source_locator, target_locator):
        """Перетаскивает элемент с одного места на другое"""
        source = self.wait_for_element_to_be_visible(source_locator)
        target = self.wait_for_element_to_be_visible(target_locator)
        ActionChains(self.driver).drag_and_drop(source, target).perform()
        return self

    def wait_for_element_to_be_visible(self, locator):
        """Ожидает, пока элемент станет видимым"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator):
        """Ожидает, пока элемент станет кликабельным"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_element(self, locator):
        """Находит первый элемент по локатору"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """Находит все элементы по локатору"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_for_custom_condition(self, condition, timeout=10):
        """Ожидает произвольное условие"""
        return WebDriverWait(self.driver, timeout).until(condition)

    def wait_for_element_to_disappear(self, locator, timeout=10):
        """Ожидает исчезновение элемента"""
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def wait_for_url_to_contain(self, partial_url, timeout=10):
        return self.wait_for_custom_condition(EC.url_contains(partial_url), timeout)

    def wait_for_url_to_be(self, url, timeout=10):
        return self.wait_for_custom_condition(EC.url_to_be(url), timeout)