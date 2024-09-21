from selenium.webdriver.common.by import By


class POMForms:
    def __init__(self, driver):

        self.driver = driver
        self.forms_xpath = "//div[@class='category-cards']//div[2]//div[1]//div[3]"

    def click_forms(self):
        self.driver.find_element(By.XPATH, self.forms_xpath).click()
