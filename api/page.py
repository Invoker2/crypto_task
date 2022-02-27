from selenium import webdriver
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from datetime import datetime

from logger import logger


class Page:
    def __init__(self,) -> object:
        self.driver = webdriver.Chrome()
        logger.info(f"[Action]: Initiating driver, please wait ...")

    def call_back_when_failed(self):
        file_path = f"./image/capture_{datetime.now()}.png"
        self.driver.get_screenshot_as_file(file_path)
        logger.info(f"[Action]: save screenshot to dir {file_path}")

    def open(self, url):
        self.driver.implicitly_wait(20)
        self.driver.get(url)
        self.driver.maximize_window()

    def is_element_displayed(self, locator):
        try:
            wait = WebDriverWait(self.driver, timeout=10)
            wait.until(lambda x: x.find_element_by_xpath(locator).is_displayed())
            return True
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException,
                ElementClickInterceptedException) as e:
            logger.error(f"[ERR] Locate element {locator} failed, due to {e.__class__.__name__}")
            self.call_back_when_failed()

    def find_element(self, locator):
        try:
            wait = WebDriverWait(self.driver, timeout=10)
            wait.until(lambda x: x.find_element_by_xpath(locator).is_displayed())
            return self.driver.find_element_by_xpath(locator)
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException,
                ElementClickInterceptedException) as e:
            logger.error(f"[ERR] Locate element {locator} failed, due to {e.__class__.__name__}")

    def click_element(self, locator):
        try:
            wait = WebDriverWait(self.driver, timeout=10)
            wait.until(lambda x: x.find_element_by_xpath(locator).is_displayed())
            element_loc = self.driver.find_element_by_xpath(locator)
            self.driver.execute_script("arguments[0].click();", element_loc)
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException,
                ElementClickInterceptedException) as e:
            logger.error(f"[ERR] Locate element {locator} failed, due to {e.__class__.__name__}")

    def scroll_down(self, by_height: object = 300) -> object:
        self.driver.execute_script(f"window.scrollBy(0, {by_height})")
        logger.info(f"[Action]: Scroll window by {by_height}")

    def exit(self):
        logger.info(f"[Action]: Closing driver, please wait ...")
        self.driver.quit()


if __name__ == "__main__":
    driver = Page()
    market_url = "https://crypto.com/exchange/markets"
    driver.open(market_url)
    driver.scroll_down(300)
    driver.exit()
