from locator import *
from element import BasePageElement

class UsernameElement(BasePageElement):
    locator = 'username'

class PasswordElement(BasePageElement):
    locator = 'password'

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    username_element = UsernameElement()
    password_element = PasswordElement()
    def is_title_matches(self):
        return "P's-Blog - Home Page" in self.driver.title

    def click_login_button(self):
        element = self.driver.find_element(*LogInPageLocators.LOGIN_BUTTON)
        element.click()
    def click_yourposts_button(self):
        element = self.driver.find_element(*MainPageLocators.YOUR_POSTS_BUTTON)
        element.click()
    def click_profile_button(self):
        element = self.driver.find_element(*MainPageLocators.PROFILE_BUTTON)
        element.click()
    def click_login_submit_button(self):
        element = self.driver.find_element(*LogInPageLocators.LOGINSUBMIT_BUTTON)
        element.click()

class LogInPage(MainPage):
    def is_login_succesfull(self):
        return self.username_element == "admin"

