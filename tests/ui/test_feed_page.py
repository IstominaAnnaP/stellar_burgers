from core.ui.pages.constructor_page import ConstructorPage
from core.ui.pages.feed_page import FeedPage
from core.ui.pages.login_page import LoginPage
from core.utils.data import UserData
import allure


class TestFeedPage:

    @allure.title('Проверка перехода на страницу конструктора по клику на кнопку Конструктор в шапке')
    def test_click_on_button_constructor(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        feed_page.click_on_button_constructor()
        constructor_page = ConstructorPage(driver)
        header = constructor_page.find_header_assemble_burger()
        assert header.text == "Соберите бургер", "Текст заголовка не соответствует ожидаемому"
   
    @allure.title('Проверка увеличения счетчика "Выполнено за всё время" при создании нового заказа')
    def test_increase_counter_all_orders_done(self, driver, create_user_with_delete):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login_user(create_user_with_delete['email'], create_user_with_delete['password'])
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        number_before = feed_page.find_counter_all_orders_done().text
        feed_page.click_on_button_constructor()
        constructor_page = ConstructorPage(driver)
        constructor_page.place_order()
        constructor_page.click_on_cross_to_close_window_order()
        constructor_page.click_on_button_feed()
        number_after = feed_page.find_counter_all_orders_done().text
        assert int(number_after) == int(number_before) + 1

    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня" при создании нового заказа')
    def test_increase_counter_today_orders_done(self, driver, create_user_with_delete):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login_user(create_user_with_delete['email'], create_user_with_delete['password'])
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        number_before = feed_page.find_counter_today_orders_done().text
        feed_page.click_on_button_constructor()
        constructor_page = ConstructorPage(driver)
        constructor_page.place_order()
        constructor_page.click_on_cross_to_close_window_order()
        constructor_page.click_on_button_feed()
        number_after = feed_page.find_counter_today_orders_done().text
        assert int(number_after) == int(number_before) + 1

    @allure.title('Проверка появления номера созданного заказа в разделе "В работе"')
    def test_created_order_appears_in_progress(self, driver, create_user_with_delete):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login_user(create_user_with_delete['email'], create_user_with_delete['password'])
        constructor_page = ConstructorPage(driver)
        constructor_page.place_order()
        number = constructor_page.find_order_number().text
        constructor_page.click_on_cross_to_close_window_order()
        constructor_page.click_on_button_feed()
        feed_page = FeedPage(driver)
        orders_in_progress = feed_page.find_order_in_progress().text
        assert number in orders_in_progress
