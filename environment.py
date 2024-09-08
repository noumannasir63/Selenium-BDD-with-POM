from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities import ConfigReader


def before_scenario(context, scenario):
    browser_name = ConfigReader.read_configuration("basic info", "browser")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        context.driver = webdriver.Chrome(
            #service=Service(ChromeDriverManager().install()),
           # options=options
        )
    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        context.driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))


def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()
