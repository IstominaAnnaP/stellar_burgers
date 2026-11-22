from selenium.webdriver.common.by import By

class LocatorsConstructorPage:
    BUTTON_FEED = [By.XPATH, './/p[text()="Лента Заказов"]']
    INGREDIENT_CARD_FLUOR_BUN = [By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]']
    CROSS_WINDOW_INGREDIENT_DETAILS = [By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//button[contains(@class, "Modal_modal__close")]']
    HEADER_ASSEMBLE_BURGER = [By.XPATH, './/h1[text()="Соберите бургер"]']
    HEADER_INGREDIENTS_DETAILS = [By.XPATH, './/h2[text()="Детали ингредиента"]']
    BASKET = [By.XPATH, './/span[@class="constructor-element__text"]']
    COUNTER_INGREDIENT_SAUCE_SPICY = [By.XPATH,'.//img[@alt="Соус Spicy-X"]/..//p[contains(@class, "counter_counter__num")]']
    BUTTON_PLACE_ORDER = [By.XPATH, './/button[text()="Оформить заказ"]']
    CROSS_WINDOW_ORDER = [By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//button[contains(@class, "Modal_modal__close")]']
    ORDER_NUMBER = [By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//p[text()="идентификатор заказа"]/preceding-sibling::h2']
    INGREDIENT_CARD_SPICY_SAUCE = [By.XPATH, './/*[@alt="Соус Spicy-X"]']
