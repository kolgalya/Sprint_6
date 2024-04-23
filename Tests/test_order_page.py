import allure
import pytest
from selenium.webdriver.common.by import By
from Pages.order_page import OrderPage as OP
from data import Urls

class TestOrderPage:
    @allure.title('Проверка нижней кнопки Заказать')
    @allure.description('На главной странице кликаем по нижней кнопки Заказать, происходит переход на форму заказа')
    def test_order_button(self, driver):
        order_page = OP(driver)
        order_page.open_page(Urls.url)
        order_page.click_cookie()
        order_page.click(OP.DOWN_ORDER_BUTTON)
        assert order_page.get_text(OP.ORDER_TITLE) == 'Для кого самокат'

    @pytest.mark.parametrize(
        'name, last_name, address, station, phone',
        [
            ('Оля', 'Парамонова', 'Москва, ул. Донская, 21', 'Сокольники', '+79563285856'),
            ('Вася', 'Ухабин', 'Москва, ул. Мосфильмовская, 4', 'Университет', '+79259996644'),
        ])

    @allure.title('Успешное оформление заказа')
    @allure.description('Кликаем по верхней кнопке Заказать, заполняем формы заказа')
    def test_order(self, driver, name, last_name, address, station, phone):
        order_page = OP(driver)
        order_page.open_page(Urls.url)
        order_page.click(OP.UP_ORDER_BUTTON)
        order_page.set_order_1(name, last_name, address, phone, station)
        driver.find_element(By.XPATH, f".//div[text() = '{station}']").click()
        order_page.set_order_2()
        order_page.click(OP.YES_BUTTON)
        assert 'Заказ оформлен' in order_page.get_text(OP.CONFIRM)

    @allure.title('Клик по лого Самокат ведет на на главную страницу «Самоката»')
    @allure.description('Переходим на страницу заказа, кликаем по лого Самокат')
    def test_logo_scooter(self, driver):
        order_page = OP(driver)
        order_page.open_page(Urls.url)
        order_page.click(OP.UP_ORDER_BUTTON)
        order_page.click(OP.LOGO_SCOOTER)
        assert order_page.get_url() == Urls.url

    @allure.title('Клик по лого Яндекс ведет на Дзен')
    @allure.description('Открываем главную страницу, кликаем по лого Яндекс')
    def test_logo_yandex(self, driver):
        order_page = OP(driver)
        order_page.open_page(Urls.url)
        order_page.click(OP.LOGO_YANDEX)
        order_page.switch_to_window()
        assert Urls.url_dzen in order_page.get_url()
















