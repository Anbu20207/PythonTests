from selenium.webdriver.common.by import By


class addtoPage:

    proceedtochkoutbutton = (By.XPATH,"//button[text()='PROCEED TO CHECKOUT']")
    addbagbutton = (By.XPATH,"//a[@class='cart-icon']/img")

    def __init__(self,driver):
        self.driver = driver

    def addbagicon(self):
        return self.driver.find_element(*addtoPage.addbagbutton)

    def chkoutbutton(self):
        return self.driver.find_element(*addtoPage.proceedtochkoutbutton)



