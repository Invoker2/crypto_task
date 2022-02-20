from selenium.webdriver.common.by import By
import pytest

class Markets:

    def __init__(self, market_name, instrument_name):
        self.market_name = market_name
        self.instrument_name = instrument_name

    def market_group_nav(self):
        market_group_nav_locator = """//div[@class="groups"]/div/div/div[text()="%s"]"""%self.market_name
        return market_group_nav_locator

    def instrument_loc(self):
        instrument_locator = """//div[@class="trade-list"]//div[@class="instrument"]//span[text()="%s"]/../../../../.."""%self.instrument_name
        return instrument_locator

    def instrument_trade(self):
        instrument_trade_locator = """//div[@class="trade-list"]//div[@class="instrument"]//span[text()="%s"]/../../../../../td[last()]//button[@type="button"]"""%self.instrument_name
        return instrument_trade_locator

if __name__ == "__main__":
    market = Markets("USDT", "BTC")
    market_group_nav = market.market_group_nav()
    print(market_group_nav)
    instrument_trade = market.instrument_trade()
    print(instrument_trade)
