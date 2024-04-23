import allure
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Pages.main_page import MainPage


class OrderPage(BasePage):
    UP_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[contains(@class, 'Button_Button')]")  # кнопка Заказать вверху страницы
    DOWN_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[contains(@class, 'Button_Button')]")  # кнопка Заказать внизу страницы
    ORDER_TITLE = (By.XPATH, "//div[contains(@class, 'Order_Header')]")  # заголовок формы бронирования
    NAME = (By.XPATH, "//input[contains(@placeholder, 'Имя')]")  # поле Имя
    LAST_NAME = (By.XPATH, "//input[contains(@placeholder, 'Фамилия')]")  # поле Фамилия
    ADDRESS = (By.XPATH, "//input[contains(@placeholder, 'Адрес')]")  # поле Адрес
    STATION = (By.XPATH, "//input[contains(@placeholder, 'Станция')]")  # поле Станция метро
    TELEPHONE = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]")  # поле Телефон
    NEXT = (By.XPATH, "//div[contains(@class, 'NextButton')]/button[contains(@class, 'Button_Button')]")  # кнопка Далее
    DATE = (By.XPATH, "//input[contains(@placeholder, 'Когда')]")  # поле Когда привезти самокат
    CALENDAR = (By.XPATH, "//div[@class = 'react-datepicker__month']/div[last()]/div[last()]")  # последний день в открывшемся календаре
    TERM = (By.XPATH, "//div[@class = 'Dropdown-placeholder']")  # поле Срок аренды
    DAYS = (By.XPATH, "//div[@class = 'Dropdown-menu']/div[last()-3]")  # четверо суток
    BLACK_COLOUR = (By.XPATH, "//input[@id = 'black']")  # чек-бокс черная неопределенность
    BUY_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text() = 'Заказать']")  # кнопка Заказать под полями в окне бронирования
    YES_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text() = 'Да']")  # кнопка Да в окне подтверждения заказа
    CONFIRM = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")  # заголовок Заказ оформлен
    LOGO_SCOOTER = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]") # лого Самокат
    LOGO_YANDEX = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]") # лого Самокат
    NEWS = (By.XPATH, "//div[contains(@class, 'floor-title__title') and text() = 'Новости']") # заголовок раздела Новости на Дзен



    @allure.step('Подтверждаем использование кук')
    def click_cookie(self):
        self.click(MainPage.COOKIE_BUTTON)

    @allure.step('Заполняем первую форму бронирования')
    def set_order_1(self, name, last_name, address, phone, station):
        self.add_text(self.NAME, name)
        self.add_text(self.LAST_NAME, last_name)
        self.add_text(self.ADDRESS, address)
        self.add_text(self.TELEPHONE, phone)
        self.click(self.STATION)
        self.add_text(self.STATION, station)

    @allure.step('Заполняем вторую форму бронирования')
    def set_order_2(self):
        self.click(self.NEXT)
        self.click(self.DATE)
        self.click(self.CALENDAR)
        self.click(self.TERM)
        self.click(self.DAYS)
        self.click(self.BLACK_COLOUR)
        self.click(self.BUY_BUTTON)

    @allure.step('Переход на вкладку Дзен')
    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait(self.NEWS)
