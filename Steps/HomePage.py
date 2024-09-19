from time import sleep

from behave import *
from selenium.webdriver.common.by import By

from Features.pages.HomePage import HomePage


@given(u'Enter DemoQA Website Address into Browser')
def step_impl(context):
    context.home_page = HomePage(context.driver)


@when(u'User Navigate on the HomePage')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


@when(u'Clicks on the Elements')
def step_impl(context):
    context.home_page.click_elements()
    sleep(3)


@when(u'Clicks on the Forms')
def step_impl(context):
    context.home_page.click_forms()
    sleep(3)

"""
@when(u'Clicks on the Alerts')
def step_impl(context):
    context.home_page.click_alerts()
    sleep(3)
"""

@when(u'Clicks on the Widgets')
def step_impl(context):
    context.home_page.click_widgets()
    sleep(3)


@when(u'Clicks on the Interactions')
def step_impl(context):
    context.home_page.click_interactions()
    sleep(3)


@when(u'Clicks on the Books')
def step_impl(context):
    context.home_page.click_books()
    sleep(3)


@then(u'Verify that elements window is opened')
def step_impl(context):
    element = context.driver.find_element(By.XPATH, "//div[@class='col-12 mt-4 col-md-6']")
    expected_text = "Please select an item from left to start practice."

    actual_text = element.text

    # Assert that the actual text matches the expected text
    assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"
