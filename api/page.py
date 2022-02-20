from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.common.by import By

class Page:
    def __init__(self,driver):
        self.driver = driver

    def open(self,url):
        self.driver.get(url)
        self.driver.maximize_window()


    def find_element(self,*loc):
        try:
            wait = WebDriverWait(self.driver,timeout = 10)
            wait.until(lambda x:x.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except TimeoutException:
            raise Exception("Time out")


    def find_elements(self,*loc):
        try:
            wait = WebDriverWait(self.driver,timeout = 10)
            wait.until(lambda x:x.find_elements(*loc).is_displayed())
            return self.driver.find_elements(*loc)
        except TimeoutException:
            raise Exception("Time out")

    def switch_iframe(self,*loc):
        name = self.driver.find_element(*loc)
        self.driver.switch_to_frame(name)

    def exit(self):
        self.driver.quit()