from selenium.webdriver.common.by import By

class LocatorsFeedPage:
    BUTTON_CONSTRUCTOR = [By.XPATH, './/p[text()="Конструктор"]']
    HEADER_FEED_ORDERS = [By.XPATH, './/h1[text()="Лента заказов"]']
    COUNTER_ALL_ORDERS_DONE = [By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p']
    COUNTER_TODAY_ORDERS_DONE = [By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p']
    ORDER_IN_PROGRESS = [By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li']
