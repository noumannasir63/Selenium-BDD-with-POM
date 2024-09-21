from behave import *
from time import sleep
from selenium.webdriver.common.by import By
from Features.pages.POM_Forms import POMForms


@when(u'Clicks on the Forms')
def step_impl(context):
    context.forms=POMForms(context.driver)
    context.forms.click_forms()
    sleep(3)