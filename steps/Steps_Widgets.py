from behave import *
from time import sleep
from selenium.webdriver.common.by import By
from pages.POM_Widgets import POMWidgets

@when(u'Clicks on the Widgets')
def step_impl(context):
    context.widgets_page=POMWidgets(context.driver)
    context.widgets_page.click_widgets()
    sleep(3)