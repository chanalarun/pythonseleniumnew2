class PurchasePage:

    def __init__(self,driver):
        self.driver=driver

        self.country_name_css='#country'
        self.country_click_xpath='//a[text()="India"]'
        self.mark_checkbox_css='div[class="checkbox checkbox-primary"] label'
        self.purchase_button_css='input[class="btn btn-success btn-lg"]'
        self.succesfull_message_css='div[class="alert alert-success alert-dismissible"]'

    def Country_name(self,country):
        self.driver.find_element_by_css_selector(self.country_name_css).clear()
        self.driver.find_element_by_css_selector(self.country_name_css).send_keys(country)

    def Select_country(self):
        self.driver.find_element_by_xpath(self.country_click_xpath).click()

    def Check_Box(self):
        self.driver.find_element_by_css_selector(self.mark_checkbox_css).click()

    def Purchase_button(self):
        self.driver.find_element_by_css_selector(self.purchase_button_css).click()

    def Succesfull_meassage(self):
       return self.driver.find_element_by_css_selector(self.succesfull_message_css).text