from selenium.webdriver.common.by import By


from PageObject.BasePage import BasePage

from Config.Config import TestData


class HomePage(BasePage):
    ADMIN=(By.XPATH,'//*[@class="oxd-text oxd-text--span oxd-main-menu-item--name" and text()="Admin"]')
    PIM = (By.XPATH,'//*[@class="oxd-text oxd-text--span oxd-main-menu-item--name" and text()="PIM"]')
    LEAVE=(By.XPATH,'//*[@class="oxd-text oxd-text--span oxd-main-menu-item--name" and text()="Leave"]')
    HEADER=(By.XPATH,'//*[@class="oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module"]')

    """constructor of page class"""
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """page action """
    def get_home_page_title(self,title):
        return self.get_title(title)

    def get_admin_icon_visible(self):
        return self.is_visible(self.ADMIN)

    def get_PIM_icon_visible(self):
        return self.is_visible(self.PIM)

    def get_LEAVE_icon_visible(self):
        return self.is_visible(self.LEAVE)

    def get_header_value(self):
        if self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)







