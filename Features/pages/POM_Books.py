from selenium.webdriver.common.by import By


class POMBooks:
    def __init__(self, driver):

        self.driver = driver
        self.books_xpath = "//div[@class='category-cards']//div[6]//div[1]//div[3]"

    def click_books(self):
        self.driver.find_element(By.XPATH, self.books_xpath).click()
