from time import sleep

from selenium.webdriver.common.by import By
from win32api import Sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Element_Attributes_POM:
    def __init__(self, driver):
        self.driver =driver

        self.text_box_nav = "//li[@id='item-0']"
        self.first_name = "userName"
        self.email = "userEmail"
        self.current_address = "currentAddress"
        self.permanent_address = "permanentAddress"
        self.submitBtn = "submit"
        self.check_box_nav = "//li[@id='item-1']"
        self.home_toggle = "//button[@title='Toggle']//*[name()='svg']"

    def text_box_navigation(self):
        self.driver.find_element(By.XPATH, self.text_box_nav).click()

    def enter_first_name(self):
            self.driver.find_element(By.ID,self.first_name).send_keys("Nouman")

    def enter_email(self):
            self.driver.find_element(By.ID,self.email).send_keys("nouman@gmail.com")

    def enter_current_address(self):
            self.driver.find_element(By.ID,self.current_address).send_keys("Lahore")

    def enter_permanent_address(self):
            self.driver.find_element(By.ID, self.permanent_address).send_keys("Islamabad")


    def click_submitBtn(self):

        # Scroll the submit button into view
        submit_button = self.driver.find_element(By.ID, self.submitBtn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

        # Wait for the submit button to be clickable and then click it
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(submit_button))
        submit_button.click()

    def text_box_click(self):
        # Get the text from the element where the result is displayed
        output_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(@id,'name')]"))
        )

        # Get the output text (e.g., "Name: Nouman")
        output_text = output_element.text

        # Remove the "Name:" prefix and strip any extra spaces
        if output_text.startswith("Name:"):
            output_text = output_text.replace("Name:", "").strip()

        # Now compare the value entered by the user with the text shown on the page
        assert output_text == "Nouman", f"Assertion failed! Expected 'Nouman', but got '{output_text}'"

    def check_box_navigation(self):
        # Scroll up to the top of the page
        self.driver.execute_script("window.scrollTo(0, 0);")
        sleep(2)  # Wait for the scroll to complete

        # Find the element and click
        element = self.driver.find_element(By.XPATH, self.check_box_nav)

        # Ensure element is visible and in viewport
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        sleep(1)  # Allow some time for scrolling to adjust

        element.click()
        sleep(3)  # Wait after clicking

    def home_toggle_Click(self):
        self.driver.find_element(By.XPATH, self.home_toggle).click()
        sleep(3)
