import allure
import pytest
from pages.main_page import MainPage as MP
from data import Urls

class TestMainPage:

    @pytest.mark.parametrize('num, result',
        [
            (0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
            (1,'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
            (2,'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
            (3,'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
            (4,'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
            (5,'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
            (6,'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
            (7,'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
        ])

    @allure.title('Проверка ответа на вопрос')
    @allure.description('На главной странице кликаем вопрос и проверяем ответ')
    def test_questions(self, driver, num, result):
        main_page = MP(driver)
        main_page.open_page(Urls.url)
        main_page.click_cookie()
        assert main_page.get_answer_text(num) == result

    @allure.title('Клик по лого Самокат ведет на на главную страницу «Самоката»')
    @allure.description('Переходим на страницу заказа, кликаем по лого Самокат')
    def test_logo_scooter(self, driver):
        main_page = MP(driver)
        main_page.open_page(Urls.url)
        main_page.click_up_order_button()
        main_page.click_scooter()
        assert main_page.get_url() == Urls.url

    @allure.title('Клик по лого Яндекс ведет на Дзен')
    @allure.description('Открываем главную страницу, кликаем по лого Яндекс')
    def test_logo_yandex(self, driver):
        main_page = MP(driver)
        main_page.open_page(Urls.url)
        main_page.click_yandex()
        main_page.switch_to_Dzen()
        assert Urls.url_dzen in main_page.get_url()
