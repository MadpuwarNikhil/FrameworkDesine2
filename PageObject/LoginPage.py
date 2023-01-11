from selenium.webdriver.common.by import By


from PageObject.BasePage import BasePage
from PageObject.HomePage import HomePage

from Config.Config import TestData


class LoginPage(BasePage):
    """By locators"""

    EMAIL =(By.NAME,"username")
    PASSWORD=(By.NAME,"password")
    LOGIN_BUTTON =(By.XPATH,'//*[@type="submit"]')
    FORGOT_PASS =(By.XPATH,'//*[@class="oxd-text oxd-text--p orangehrm-login-forgot-header"]')

    """constructor of page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page actions"""
    """this is use to get a page tittle"""
    def get_login_page(self, title):
        return self.get_title(title)

    """this is use to check forgot pass link"""
    def is_forgot_link_exist(self):
        return self.is_visible(self.FORGOT_PASS)

    """this is use to login to application"""
    def do_login(self,username,password):
        self.do_send_keys(self.EMAIL,username)
        self.do_send_keys(self.PASSWORD,password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)



