from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver


class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def do_click(self,by_locator):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(by_locator)).click()

    def do_sendKeys(self,by_locator,testData):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).send_keys(testData)

    def do_getText(self,by_locator):
        getText = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).text
        return getText

    def do_selectFromDropdownByText(self,by_locator,testData):
        el = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        dd = Select(el)
        dd.select_by_visible_text(testData)

    def do_selectFromDropdown(self,by_locator,testData):
        el = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        dd = Select(el)
        dd.select_by_index(testData)

    def is_ElementPresent(self,by_locator):
        elementPresent = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).is_displayed()
        return elementPresent

    def hit_Enter(self,by_locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.ENTER)

    def hit_Tab(self,by_locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.TAB)