
class Urls:
    BASE_URL = "https://stellarburgers.nomoreparties.site/"
    LOGIN_PAGE = f"{BASE_URL}login"
    FORGOT_PASSWORD = f"{BASE_URL}forgot-password"
    RESET_PASSWORD = f"{BASE_URL}reset-password"
    PERSONAL_ACCOUNT_PAGE = f"{BASE_URL}account"
    ORDER_FEED = f"{BASE_URL}feed"
    ORDER_HISTORY = f"{BASE_URL}account/order-history"
    INGREDIENT_DETAILS = f"{BASE_URL}ingredient"

    # API endpoints
    REGISTER_API = f"{BASE_URL}api/auth/register"
    LOGIN_API = f"{BASE_URL}api/auth/login"
    DELETE_USER = f"{BASE_URL}api/auth/user"
    INGREDIENTS_API = f"{BASE_URL}api/ingredients"
    CREATE_ORDER_API = f"{BASE_URL}api/orders"