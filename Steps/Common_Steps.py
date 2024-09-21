from time import sleep

from behave import *
from selenium.webdriver.common.by import By

from Features.pages.POM_Common_Steps import CommonSteps


@given(u'Enter DemoQA Website Address into Browser')
def step_impl(context):
    context.home_page = CommonSteps(context.driver)


@when(u'User Navigate on the HomePage')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

"""
@then(u'Verify that elements window is opened')
def step_impl(context):
    element = context.driver.find_element(By.XPATH, "//div[@class='col-12 mt-4 col-md-6']")
    expected_text = "Please select an item from left to start practice."

    actual_text = element.text

    # Assert that the actual text matches the expected text
    assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"
    
    """
