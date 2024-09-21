from behave import *
from time import sleep
from selenium.webdriver.common.by import By
from Features.pages.POM_Interactions import POMInteractions


@when(u'Clicks on the Interactions')
def step_impl(context):
    context.interaction=POMInteractions(context.driver)
    context.interaction.click_interactions()
    sleep(3)