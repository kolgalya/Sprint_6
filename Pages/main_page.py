import allure
from Pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    UP_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[contains(@class, 'Button_Button')]")  # кнопка Заказать вверху страницы
    DOWN_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[contains(@class, 'Button_Button')]")  # кнопка Заказать внизу страницы
    COOKIE_BUTTON = (By.XPATH, '//*[@id="rcc-confirm-button"]')  # кнопка подтверждения использования кук
    QUESTIONS = (By.XPATH, '//*[@id="accordion__heading-{}"]')  # универсальный локатор для вопросов
    ANSWER = (By.XPATH, '//*[@id="accordion__panel-{}"]')  # универсальный локатор для ответов
    LOGO_SCOOTER = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]") # лого Самокат
    LOGO_YANDEX = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]") # лого Яндекс
    NEWS = (By.XPATH, "//div[contains(@class, 'floor-title__title') and text() = 'Новости']")  # заголовок раздела Новости на Дзен

    @allure.step('Подтверждаем использование кук')
    def click_cookie(self):
        self.click(self.COOKIE_BUTTON)

    @allure.step('Преобразовываем универсальные локаторы вопроса и ответа, получаем текст ответа')
    def get_answer_text(self, num):
        locator_q = self.format_locators(self.QUESTIONS, num)
        locator_a = self.format_locators(self.ANSWER, num)
        self.click(locator_q)
        return self.get_text(locator_a)

    @allure.step('Клик по верхней кнопки Заказать')
    def click_up_order_button(self):
        self.click(self.UP_ORDER_BUTTON)

    @allure.step('Клик по нижней кнопки Заказать')
    def click_down_order_button(self):
        self.click(self.DOWN_ORDER_BUTTON)

    @allure.step('Клик по лого Самокат')
    def click_scooter(self):
        self.click(self.LOGO_SCOOTER)

    @allure.step('Клик по лого Яндекс')
    def click_yandex(self):
        self.click(self.LOGO_YANDEX)

    @allure.step('Переход на вкладку Дзен')
    def switch_to_Dzen(self):
        self.switch_to_window(self.NEWS)
