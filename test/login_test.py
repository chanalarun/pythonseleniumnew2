import allure
import moment


from selenium import webdriver
import time
import pytest
from pages.AddCartPage import AddToCart
from pages.checkoutpage import CheckOutPage
from pages.purchasepage import PurchasePage
from utils import utils

@pytest.mark.usefixtures("test_setup")
class TestEcom:


    def test_AddToCart(self):
        driver=self.driver
        addtocart=AddToCart(driver)
        addtocart.enter_shop()
        addtocart.cart_button()

    def test_checkOut(self):
        driver=self.driver
        checkout=CheckOutPage(driver)
        checkout.checkout1()
        checkout.checkout2()

    def test_Purchase(self):
        try:
            driver=self.driver
            purchase=PurchasePage(driver)
            purchase.Country_name(utils.country)
            time.sleep(5)
            purchase.Select_country()
            purchase.Check_Box()
            purchase.Purchase_button()
            purchase.Succesfull_meassage()


        except:
            print("error occured")
            curtime = moment.now().strftime("%H-%M-%S : %d-%m-%y")
            testname =utils.whoami()
            screenshortName=testname+"_"+curtime
            allure.attach(self.driver.get_screenshot_as_png(),name=screenshortName,attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/hp/PycharmProjects/pyhonseleniymframe/screenshorts"+screenshortName+".png")



            raise

        else:
            print("no exception")

        finally:
            print("I am inside finally block")


