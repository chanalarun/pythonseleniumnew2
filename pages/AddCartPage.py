import pytest


class AddToCart:

    def __init__(self,driver):
        self.driver=driver

        self.shop_button_xpath='//a[text()="Shop"]'
        self.cart_button_css='button[class="btn btn-info"]'

    def enter_shop(self):
       self.driver.find_element_by_xpath( self.shop_button_xpath).click()

    def cart_button(self):
        products = self.driver.find_elements_by_css_selector(self.cart_button_css)
        for product in products:
            product.click()
