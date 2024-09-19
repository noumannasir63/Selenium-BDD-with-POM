from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

        self.elements_xpath = "//div[@class='category-cards']//div[1]//div[1]//div[3]"
        self.forms_xpath = "//div[@class='category-cards']//div[2]//div[1]//div[3]"
        #self.alerts_xpath = "//div[@class='category-cards']//div[3]//div[1]//div[3]"
        self.widgets_xpath = "//div[@class='category-cards']//div[4]//div[1]//div[3]"
        self.interactions_xpath = "//div[@class='category-cards']//div[5]//div[1]//div[3]"
        self.books_xpath = "//div[@class='category-cards']//div[6]//div[1]//div[3]"

    def click_elements(self):
        self.driver.find_element(By.XPATH, self.elements_xpath).click()

    def click_forms(self):
        self.driver.find_element(By.XPATH, self.forms_xpath).click()

    def click_widgets(self):
        self.driver.find_element(By.XPATH, self.widgets_xpath).click()


    def click_interactions(self):
        self.driver.find_element(By.XPATH, self.interactions_xpath).click()


    def click_books(self):
        self.driver.find_element(By.XPATH, self.books_xpath).click()
"""
    def click_alerts(self):
        self.driver.find_element(By.XPATH, self.alerts_xpath).click()
"""