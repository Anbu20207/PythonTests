from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


class homePage:

    search = (By.XPATH, "//input[@type='search']")
    displayitems = (By.XPATH, "//div[@class='product']")
    addtocart = (By.XPATH,"//div[@class='product-action']/button")

    def __init__(self, driver):
        self.driver = driver

    def searchitems(self):
        # * to read search as tuple and deserialises.
        return self.driver.find_element(*homePage.search)

    def displayitemsmtd(self):
        count = len(self.driver.find_elements(*homePage.displayitems))
        return count

    def addtocartmtd(self):
        return self.driver.find_elements(*homePage.addtocart)


