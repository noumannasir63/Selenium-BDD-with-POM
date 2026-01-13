from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities import ConfigReader
from selenium.webdriver.edge.options import Options



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
        options = Options()
        options.add_argument("--headless=new")  # optional but recommended
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        context.driver = webdriver.Edge(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()

# "Just for Test4"

