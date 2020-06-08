from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    iPhone = (By.CSS_SELECTOR, "[href='/iphone/")

    def iPhone_navigation(self):

        return self.driver.find_element(*Homepage.iPhone)