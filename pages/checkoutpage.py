class CheckOutPage:

    def __init__(self,driver):
        self.driver=driver

        self.checkout1_button_css='a[class="nav-link btn btn-primary"]'
        self.checkout2_button_xpath='//button[@class="btn btn-success"]'

    def checkout1(self):
        self.driver.find_element_by_css_selector(self.checkout1_button_css).click()

    def checkout2(self):
        self.driver.find_element_by_xpath(self.checkout2_button_xpath).click()


