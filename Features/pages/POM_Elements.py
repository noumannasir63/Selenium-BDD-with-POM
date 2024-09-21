from selenium.webdriver.common.by import By


class POMElements:
    def __init__(self, driver):

        self.driver = driver
        self.elements_xpath = "//div[@class='category-cards']//div[1]//div[1]//div[3]"

    def click_elements(self):
        self.driver.find_element(By.XPATH, self.elements_xpath).click()
