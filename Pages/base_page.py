import allure
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Ожидание элемента и его выбор')
    def wait (self, locator):
        WDW(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу')
    def click(self, locator):
        WDW(self.driver, 5).until(EC.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Ввод текста')
    def add_text(self, locator, text):
        WDW(self.driver, 5).until(EC.visibility_of_element_located(locator))
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получить текст')
    def get_text(self, locator):
        WDW(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    @allure.step('Изменение универсального локатора')
    def format_locators(self, locator_1, num):
        method, locator = locator_1          #'//*[@id="accordion__heading-{}"]'
        locator = locator.format(num)        #'//*[@cid="accordion__heading-1"]'
        return (method, locator)

    @allure.step('Получить url')
    def get_url(self):
        return self.driver.current_url