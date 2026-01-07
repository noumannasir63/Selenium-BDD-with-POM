from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CommonSteps:
    def __init__(self, driver):
        self.driver = driver

    def is_elements_window_opened(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[@class='col-12 mt-4 col-md-6']")
            )
        )

        expected_text = "Please select an item from left to start practice."
        return element.text == expected_text