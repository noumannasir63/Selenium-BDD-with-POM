from selenium.webdriver.common.by import By

class Element_Attributes_POM:
    def __init__(self, driver):
        self.driver =driver

        self.text_box = "//li[@id='item-0']"
        self.first_name = "userName"
        self.email = "userEmail"
        self.current_address = "currentAddress"
        self.permanent_address = "permanentAddress"
        self.submitBtn = "submit"

    def enter_first_name(self):
            self.driver.find_element(By.ID,self.first_name).send_keys("Nouman")

    def enter_email(self):
            self.driver.find_element(By.ID,self.email).send_keys("nouman@gmail.com")

    def enter_current_address(self):
            self.driver.find_element(By.ID,self.current_address).send_keys("Lahore")

    def enter_permanent_address(self):
            self.driver.find_element(By.ID, self.permanent_address).send_keys("Islamabad")

    def click_submitBtn(self):
            self.driver.find_element(By.ID, self.submitBtn).click()

    def text_box_click(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH, "//div[@class='category-cards']//div[1]//div[1]//div[3]").click()
        self.driver.find_element(By.XPATH, self.text_box).click()


