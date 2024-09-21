from selenium.webdriver.common.by import By


class POMInteractions:
    def __init__(self, driver):

        self.driver = driver
        self.interactions_xpath = "//div[@class='category-cards']//div[5]//div[1]//div[3]"

    def click_interactions(self):
        self.driver.find_element(By.XPATH, self.interactions_xpath).click()
