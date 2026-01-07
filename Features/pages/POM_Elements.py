from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class POMElements:
    def __init__(self, driver):

        self.driver = driver
        self.elements_xpath = "//div[@class='category-cards']//div[1]//div[1]//div[3]"

    def click_elements(self):
        wait = WebDriverWait(self.driver, 10)   # ✅ yahan local wait
        element = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.elements_xpath))
        )
        element.click()
