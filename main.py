import unittest
from selenium import webdriver
import page

class PythonOrgTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://www.myprogrammershub.com")

    def test_title(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()

    def test_log_in_on_programmershub_com(self):
        loginPage = page.LogInPage(self.driver)
        mainPage = page.MainPage(self.driver)
        mainPage.click_login_button()
        mainPage.username_element= "admin"
        x = "admin"
        mainPage.password_element = "Benzah12"
        mainPage.click_login_submit_button()

        mainPage.click_profile_button()
        assert loginPage.is_login_succesfull()



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()