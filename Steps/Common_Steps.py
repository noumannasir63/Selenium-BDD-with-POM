from behave import *
from Features.pages.POM_Common_Steps import CommonSteps


@given('Enter DemoQA Website Address into Browser')
def step_open_website(context):
    context.common_page = CommonSteps(context.driver)


@when('User Navigate on the HomePage')
def step_navigate_home(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


@then('Verify that elements window is opened')
def step_verify_elements_window(context):
    assert context.common_page.is_elements_window_opened(), \
        "Elements window is not opened"
