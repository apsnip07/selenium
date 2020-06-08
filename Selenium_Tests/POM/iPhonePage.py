from selenium.webdriver.common.by import By


class iPhonePage:

    def __init__(self, driver):
        self.driver = driver

    models = (By.XPATH, "//span[@class='chapternav-label'][contains(text(),'iPhone')]")

    def IdentifyModels(self):

        str = []
        item = -1
        return self.driver.find_elements(*iPhonePage.models)