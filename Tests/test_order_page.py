import allure
import pytest
from selenium.webdriver.common.by import By
from Pages.main_page import MainPage as MP
from Pages.order_page import OrderPage as OP
from data import Urls

class TestOrderPage:
    @allure.title('Проверка нижней кнопки Заказать')
    @allure.description('На главной странице кликаем по нижней кнопки Заказать, происходит переход на форму заказа')
    def test_order_button(self, driver):
        main_page = MP(driver)
        main_page.open_page(Urls.url)
        main_page.click_cookie()
        main_page.click_down_order_button()
        order_page = OP(driver)
        assert order_page.order_title() == 'Для кого самокат'

    @pytest.mark.parametrize(
        'name, last_name, address, station, phone',
        [
            ('Оля', 'Парамонова', 'Москва, ул. Донская, 21', 'Сокольники', '+79563285856'),
            ('Вася', 'Ухабин', 'Москва, ул. Мосфильмовская, 4', 'Университет', '+79259996644'),
        ])

    @allure.title('Успешное оформление заказа')
    @allure.description('Кликаем по верхней кнопке Заказать, заполняем формы заказа')
    def test_order(self, driver, name, last_name, address, station, phone):
        main_page = MP(driver)
        main_page.open_page(Urls.url)
        main_page.click_cookie()
        main_page.click_up_order_button()
        order_page = OP(driver)
        order_page.set_order_1(name, last_name, address, phone, station)
        driver.find_element(By.XPATH, f".//div[text() = '{station}']").click()
        order_page.set_order_2()
        order_page.yes_order()
        assert 'Заказ оформлен' in order_page.confirm_title()
