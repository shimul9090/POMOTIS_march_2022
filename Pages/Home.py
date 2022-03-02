import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    new_link = (By.LINK_TEXT,"New")
    opp_link = (By.LINK_TEXT,"Opportunity")

    def clickOpp(self):
        while(True):
            try:
                self.do_click(self.new_link)
                break
            except:
                time.sleep(2)
                continue
        self.do_click(self.opp_link)