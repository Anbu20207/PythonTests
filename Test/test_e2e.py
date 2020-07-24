import time

import pytest
#import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from Utilities.BaseClass import BaseClass
from pageObjects.PlaceOrderPage import PlaceOrderPage
from pageObjects.addtoPage import addtoPage
from pageObjects.homePage import homePage


class TestOne(BaseClass):

    def test_e2e(self):
        obj = homePage(self.driver)
        objproceedtochk = addtoPage(self.driver)
          objplaceorderpage = PlaceOrderPage(self.driver)
        obj.searchitems().send_keys("be")
        time.sleep(4)
        count = obj.displayitemsmtd()
        print(count)
        count1 = len(obj.addtocartmtd())
        print(count1)
        for i in obj.addtocartmtd():
            i.click()
        objproceedtochk.addbagicon().click()
        objproceedtochk.chkoutbutton().click()

        self.waitmtd("promocode")

        objplaceorderpage.procode().send_keys("rahulshettyacademy")
        objplaceorderpage.probtn().click()

        time.sleep(8)
        #message = self.driver.find_element_by_class_name("promoInfo").text
        print(self.driver.find_element_by_class_name("promoInfo").text)
        #print("The promo code message:" + message)
    # assert message in "applied"
    # instance variable should be called using self bcox they are part of object constructor
    # and class variable should be called using class name dot
    # instance variables are declared in constructor are called by self

