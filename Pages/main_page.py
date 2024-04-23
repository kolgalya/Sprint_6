import allure
from Pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    COOKIE_BUTTON = (By.XPATH, '//*[@id="rcc-confirm-button"]')  # кнопка подтверждения использования кук
    QUESTIONS = (By.XPATH, '//*[@id="accordion__heading-{}"]')  # универсальный локатор для вопросов
    ANSWER = (By.XPATH, '//*[@id="accordion__panel-{}"]')  # универсальный локатор для ответов

    @allure.step('Подтверждаем использование кук')
    def click_cookie(self):
        self.click(self.COOKIE_BUTTON)

    @allure.step('Преобразовываем универсальные локаторы вопроса и ответа, получаем текст ответа')
    def get_answer_text(self, num):
        locator_q = self.format_locators(self.QUESTIONS, num)
        locator_a = self.format_locators(self.ANSWER, num)
        self.click(locator_q)
        return self.get_text(locator_a)
