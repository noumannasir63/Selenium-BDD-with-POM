from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions

from utilities import ConfigReader


def before_scenario(context,driver):
    browser_name= ConfigReader.read_configuration("basic info","browser")
    if browser_name == "chrome":
     options = webdriver.ChromeOptions()
     context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        # Automatically download and set up Edge WebDriver
        context.driver = webdriver.Edge(EdgeChromiumDriverManager().install(), options=options)

    #context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic info","url"))

def after_scenario(context,driver):
    context.driver.quit()