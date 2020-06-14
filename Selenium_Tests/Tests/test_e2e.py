import time
from logging import exception

import pytest

from POM.Homepage import Homepage
from POM.SelectSpecs import Specs
from POM.iPhonePage import iPhonePage
from Utilities.BaseClass import BaseClass
from Utilities.Test_LoggingMethod import Logs


class Test_e2e(BaseClass, Logs):

    def test_e2e(self,get_data):
        log = self.logger()
        log.info("***Test user is able to select a {} {} iPhone SE***".format(get_data["color"], get_data["memory"]))
        log.info("Navigating to www.apple.com")
        try:
            self.driver.get("https://www.apple.com/")
            self.driver.maximize_window()
            homepage = Homepage(self.driver)
            log.info("Click on iPhone link")
            homepage.iPhone_navigation().click()

            iphones = iPhonePage(self.driver)
            models = iphones.IdentifyModels()
            str = []
            item = -1
            log.info("Iterate through iphone models")

            for model in models:
                str.append(model.text)
                log.info("Model {}".format(model.text))
                item = item + 1
                if model.text == 'iPhone SE':
                    model.click()
                    break

            self.driver.find_element_by_css_selector("[data-analytics-title='buy iphone se']").click()
            # Select iPhone SE Specs
            specs = Specs(self.driver)

            specs.Color(get_data["color"])
            time.sleep(5)
            specs.Capacity(get_data["memory"])
            time.sleep(5)
            specs.serviceprovider("Unlocked")
            time.sleep(5)
            specs.TradeInValue("No")
            time.sleep(5)
            specs.checkout()
            log.info("Added iphone to cart")
            log.removeHandler(self)

        except Exception as e:

            log.error("Error {}".format(e))
            pytest.fail("{}".format(e))

    @pytest.fixture(params=[{"color": "Red", "memory": "128gb"}, {"color":"White", "memory": "128gb"}])
    def get_data(self, request):
        return request.param
