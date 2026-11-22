class Urls:
    MAIN_URL = 'https://stellarburgers.education-services.ru'

    #API эндпоинты
    REGISTER_ENDPOINT = f'{MAIN_URL}/api/auth/register'
    DELETE_USER_ENDPOINT = f'{MAIN_URL}/api/auth/user'
    LOGIN_ENDPOINT = f'{MAIN_URL}/api/auth/login'
    MAKE_ORDER_ENDPOINT = f'{MAIN_URL}/api/orders'

    #UI страницы
    FEED_URL = f"{MAIN_URL}/feed"
    LOGIN_URL = f"{MAIN_URL}/login"