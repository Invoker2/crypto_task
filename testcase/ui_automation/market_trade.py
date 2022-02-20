from selenium import webdriver
from page import Page
import time
import pytest
from element_location import Markets


@pytest.mark.parametrize("market_name, instrument_name",
                         [
                             # ("USDT","BTC"),
                             ("USDT","ZIL"),
                         ])
def test_instrument_trade(market_name, instrument_name):
    url = "https://crypto.com/exchange/markets"
    obj = Page()
    obj.open(url)
    market = Markets(market_name, instrument_name)
    market_group_nav = market.market_group_nav()
    obj.click_element(market_group_nav)
    instrument_locator = market.instrument_loc()
    try:
        if obj.is_element_displayed(instrument_locator):
            instrument_trade_locator = market.instrument_trade()
            time.sleep(2)
            obj.click_element(instrument_trade_locator)
        else:
            obj.scroll_down(300)
    finally:
        obj.exit()
