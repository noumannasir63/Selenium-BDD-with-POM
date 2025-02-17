from selenium.webdriver.common.by import By


class POMAlerts:
    def __init__(self, driver):

        self.driver = driver
        self.alerts_xpath = "//div[@class='category-cards']//div[3]//div[1]//div[3]"

    def click_alerts(self):
        self.driver.find_element(By.XPATH, self.alerts_xpath).click()
