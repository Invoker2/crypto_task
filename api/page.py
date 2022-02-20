from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.common.by import By
from logger import logger

class Page:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open(self,url):
        self.driver.get(url)
        self.driver.maximize_window()
        logger.info("Open url success!")

    def is_element_displayed(self, locator):
        try:
            wait = WebDriverWait(self.driver,timeout = 10)
            wait.until(lambda x:x.find_element_by_xpath(locator).is_displayed())
            logger.info("Element is visible")
            return True
        except TimeoutException:
            raise Exception("Time out")

    def find_element(self, locator):
        try:
            wait = WebDriverWait(self.driver,timeout = 10)
            wait.until(lambda x:x.find_element_by_xpath(locator).is_displayed())
            return self.driver.find_element_by_xpath(locator)
        except TimeoutException:
            raise Exception("Time out")

    def click_element(self,locator):
        try:
            wait = WebDriverWait(self.driver,timeout = 10)
            wait.until(lambda x:x.find_element_by_xpath(locator).is_displayed())
            return self.driver.find_element_by_xpath(locator).click()
        except TimeoutException:
            raise Exception("Time out")

    def scroll_down(self, height: object = 300) -> object:
        self.driver.execute_script("window.scrollBy(0, %s)"%height)

    def exit(self):
        self.driver.quit()