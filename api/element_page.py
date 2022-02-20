from selenium import webdriver
from selenium.webdriver.common.by import By

import time as t
from page import Page

class LoginPage(Page):

    _iframe_loc = (By.XPATH,"//div[@id='normalLoginTab']/div[0]/div[0]/iframe")
    _user_loc = (By.XPATH,'//input[@name="email" and @data-loginname="loginEmail"]')
    _paw_loc = (By.XPATH,'//input[@name="password" and @placeholder="输入密码"]')
    _logbt_loc = (By.ID,"dologin")

    def user_input(self,username):
        self.switch_iframe(*self._iframe_loc)
        self.find_element(*self._user_loc).send_key(username)
        return username

    def paw_input(self,password):
        self.find_element(*self._paw_loc).send_key(password)

    def login_button(self):
        self.find_element(*self._logbt_loc).click()