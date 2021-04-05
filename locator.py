from selenium.webdriver.common.by import By

class MainPageLocators(object):
    HOME_BUTTON = (By.ID, 'list-home-list')
    YOUR_POSTS_BUTTON = (By.ID, 'list-settings-list')
    PROFILE_BUTTON = (By.ID, 'list-profile-list')
class LogInPageLocators(object):
    LOGIN_BUTTON = (By.ID, 'log-in')
    LOGINSUBMIT_BUTTON = (By.CLASS_NAME, 'BTN')