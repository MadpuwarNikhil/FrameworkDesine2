
from PageObject.HomePage import HomePage
from PageObject.LoginPage import LoginPage


from Config.Config import TestData
from Test.test_base import BaseTest


class Test_Home(BaseTest):

    def test_home_page_title(self):
        self.loginPage=LoginPage(self.driver)
        homePage=self.loginPage.do_login(TestData.USE_RNAME,TestData.PASSWORD)
        title =homePage.get_home_page_title(TestData.HOMEPAGE_TITLE)
        assert title==TestData.HOMEPAGE_TITLE



    def test_admin_visible(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USE_RNAME, TestData.PASSWORD)
        flag=homePage.get_admin_icon_visible()
        assert flag

    def test_PIM_visible(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USE_RNAME, TestData.PASSWORD)
        flag = homePage.get_PIM_icon_visible()
        assert flag

    def test_LEAVE_visible(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USE_RNAME, TestData.PASSWORD)
        flag=homePage.get_LEAVE_icon_visible()
        assert flag

    def test_header(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USE_RNAME, TestData.PASSWORD)
        header=homePage.get_header_value()
        assert header==TestData.HOME_PAGE_HEADER

