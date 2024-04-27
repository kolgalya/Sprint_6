import allure
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class OrderPage(BasePage):
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

    @allure.step('Получаем текст заголовка формы бронирования')
    def order_title(self):
        return self.get_text(self.ORDER_TITLE)

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

    @allure.step('Подтверждаем оформление заказа')
    def yes_order(self):
        self.click(self.YES_BUTTON)

    @allure.step('Получаем текст заголовка окна "Заказ оформлен"')
    def confirm_title(self):
        return self.get_text(self.CONFIRM)

