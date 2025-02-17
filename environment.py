from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities import ConfigReader


def before_all(context):
    """
    This hook will run once before all feature files and scenarios.
    It will open the browser and share the same session for all scenarios.
    """
    browser_name = ConfigReader.read_configuration("basic info", "browser")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()

        # Ensure compatibility with the latest Selenium version
        chrome_service = Service(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=chrome_service, options=options)

    elif browser_name == "edge":
        options = webdriver.EdgeOptions()

        edge_service = Service(EdgeChromiumDriverManager().install())
        context.driver = webdriver.Edge(service=edge_service, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))


def after_all(context):
    """
    This hook will run once after all feature files and scenarios.
    It will close the browser after all tests are done.
    """
    if hasattr(context, 'driver'):
        context.driver.quit()
