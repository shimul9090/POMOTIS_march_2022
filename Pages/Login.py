from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    user_name = (By.ID,"username")
    user_password = (By.ID,"password")
    login_btn = (By.NAME,"login-submit")

    def application_Login(self,username,password):
        self.do_sendKeys(self.user_name,username)
        self.do_sendKeys(self.user_password,password)
        self.do_click(self.login_btn)