from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Specs:

    def __init__(self, driver):
        self.driver = driver

    def TradeInValue(self, TradeInValue):
        if TradeInValue == "No":
            trade_in_option = (By.CSS_SELECTOR, "[value='noTradeIn']")
            trade_in_option = self.driver.find_element(*trade_in_option)
            self.driver.execute_script("arguments[0].click();", trade_in_option)


    def Color(self, usercolor):
        if usercolor == "Red":
            color = (By.CSS_SELECTOR, "[id='Item1product_red_label']")
        elif usercolor == "White":
            color = (By.CSS_SELECTOR, "[id='dimensionColor-white']")
        color=self.driver.find_element(*color)
        self.driver.execute_script("arguments[0].click();", color)

    def Capacity(self, memory):
            if memory == "128gb":
                capacity = (By.CSS_SELECTOR, "[for*='128gb']")
                self.driver.find_element(*capacity).click()

    def serviceprovider(self, carrier):
            if carrier == "Unlocked":
                carrier = (By.CSS_SELECTOR, "[id*='Item4-carrierModel-UNLOCKED/US']")
                element = self.driver.find_element(*carrier)
                self.driver.execute_script("arguments[0].click();", element)

    def checkout(self):
        buy_button = (By.CSS_SELECTOR, "[name= 'add-to-cart']")
        buy_button=self.driver.find_element(*buy_button)
        self.driver.execute_script("arguments[0].click();", buy_button)





