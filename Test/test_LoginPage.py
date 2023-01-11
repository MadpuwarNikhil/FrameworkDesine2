import pytest

from PageObject.LoginPage import LoginPage

from Config.Config import TestData
from Test.test_base import BaseTest


class Test_Login(BaseTest):
    def test_forgot_pass_is_visible(self):
        self.loginPage=LoginPage(self.driver)
        flag=self.loginPage.is_forgot_link_exist()
        assert flag

    def test_login_page_title(self):
        self.loginPage=LoginPage(self.driver)
        title=self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title== TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginPage=LoginPage(self.driver)
        self.loginPage.do_login(TestData.USE_RNAME,TestData.PASSWORD)
