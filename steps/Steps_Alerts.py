from behave import *
from time import sleep
from selenium.webdriver.common.by import By
from pages.POM_Alerts import POMAlerts


@when(u'Clicks on the Alerts')
def step_impl(context):
    context.alerts_page=POMAlerts(context.driver)
    context.alerts_page.click_alerts()
    sleep(3)
