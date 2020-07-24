from selenium.webdriver.common.by import By


class PlaceOrderPage:
    promocode = (By.CLASS_NAME,"promoCode")
    promobtn1 = (By.CLASS_NAME, "promobtn")

    def __init__(self,driver):
        self.driver = driver

    def procode(self):
        return self.driver.find_element(*PlaceOrderPage.promocode)

    def probtn(self):
        return self.driver.find_element(*PlaceOrderPage.promobtn1)


