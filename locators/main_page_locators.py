from selenium.webdriver.common.by import By

class MainPageLocators:
    INGREDIENT_SECTION = (By.CSS_SELECTOR, "section.BurgerIngredients_ingredients__1N8v2")
    INGREDIENT_NAME = (By.CSS_SELECTOR, "p.BurgerIngredient_ingredient__text__yp3dH")
    INGREDIENT_ITEM = (By.XPATH, "//img[@alt='Краторная булка N-200i']")
    # Для динамического поиска ингредиента
    ORDER_ZONE = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket')]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_LINK = (By.XPATH, "//p[text()='Лента Заказов']")

    # Модальное окно ингредиента
    INGREDIENT_MODAL = (By.CLASS_NAME, "Modal_modal__contentBox__sCy8X")
    INGREDIENT_DETAILS = (By.CSS_SELECTOR, "img.BurgerIngredient_ingredient__image__3e-07")
    CLOSE_MODAL_BUTTON = (By.CSS_SELECTOR, "button.Modal_modal__close__TnseK")
    MODAL_CLOSE_INGREDIENTS = (By.CSS_SELECTOR, "button[type='button'].Modal_modal__close__TnseK")

    # Модальные окна
    ORDER_NUMBER = (By.CSS_SELECTOR, "div.OrderDetails_number__1xWqK")
    ORDER_MODAL = (By.CSS_SELECTOR, "div.Modal_modal__P3_V5")
    MODAL_LOADING_ANIMATION = (By.CSS_SELECTOR, "img[alt='loading animation']")

    # Локаторы для счетчика
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "p[class^='counter_counter__num']")

    # Локатор для номера заказа в модальном окне
    ORDER_NUMBER_MODAL = (By.CSS_SELECTOR, "h2.Modal_modal__title__2L34m.text_type_digits-large")

    # Локатор для номера заказов в разделе "В работе"
    IN_PROGRESS_ORDER = "li.text.text_type_digits-default.mb-2"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    PROFILE_SECTION = (By.XPATH, "//a[text()='Профиль']")