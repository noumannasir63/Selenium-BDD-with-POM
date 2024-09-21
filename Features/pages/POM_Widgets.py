from selenium.webdriver.common.by import By


class POMWidgets:
    def __init__(self, driver):

        self.driver = driver
        self.widgets_xpath = "//div[@class='category-cards']//div[4]//div[1]//div[3]"

    def click_widgets(self):
        self.driver.find_element(By.XPATH, self.widgets_xpath).click()
