from selenium.webdriver.common.by import By

class LocatorsLoginPage:
    BUTTON_LOGIN = [By.XPATH, './/button[text()="Войти"]']
    EMAIL_FIELD = [By.XPATH, './/input[@name="name"]']
    PASSWORD_FIELD = [By.XPATH, './/input[@name="Пароль"]']
