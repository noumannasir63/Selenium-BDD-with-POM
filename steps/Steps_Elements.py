from behave import *
from time import sleep
from selenium.webdriver.common.by import By
from pages.POM_Elements import POMElements


@when(u'Clicks on the Elements')
def step_impl(context):
    context.elements_page=POMElements(context.driver)
    context.elements_page.click_elements()
    sleep(3)
