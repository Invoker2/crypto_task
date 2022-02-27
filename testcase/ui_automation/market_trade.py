from page import Page
import time
import pytest
from element_location import Markets
from logger import logger


class TestMarketTrade:
    driver = None
    market_url = "https://crypto.com/exchange/markets"

    def setup_class(self):
        # initiate chrome
        self.driver = Page()

    def teardown_class(self):
        # driver close
        self.driver.exit()
        logger.info("[Tear Down]: Close driver and quit")


    def setup(self):
        # navigate to page
        self.driver.open(self.market_url)
        logger.info(f"[Set Up]: Open driver and navigate to {self.market_url}")

    def teardown(self):
        pass

    @pytest.mark.parametrize("market_name, instrument_name",
                             [
                                 ("USDT", "ZIL"),
                                 ("USDT", "BTC")
                             ])
    def test_instrument_trade(self, market_name, instrument_name):
        market = Markets(market_name, instrument_name)
        self.driver.click_element(market.market_group_nav)
        if self.driver.is_element_displayed(market.instrument_loc):
            logger.info("Element is visible, continue checking ...")
            self.driver.click_element(market.instrument_trade)
            # time.sleep(20)
            assert True
        else:
            logger.info("Element is invisible, case failed...")
            assert False
