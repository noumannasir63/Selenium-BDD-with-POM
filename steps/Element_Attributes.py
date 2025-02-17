from behave import *
from time import sleep


from pages.ELement_Attributes_POM import Element_Attributes_POM

@given(u'Element Dropdown is open and clicks on Text Box Attribute')
def step_impl(context):
    context.elements_attributes = Element_Attributes_POM(context.driver)
    context.elements_attributes.text_box_navigation()
    sleep(3)


@when(u'User give first name')
def step_impl(context):
    context.elements_attributes.enter_first_name()


@when(u'User give Email of Text Box')
def step_impl(context):
    context.elements_attributes.enter_email()


@when(u'User provide current Address')
def step_impl(context):
    context.elements_attributes.enter_current_address()


@when(u'User provide permanent Address')
def step_impl(context):
    context.elements_attributes.enter_permanent_address()


@when(u'User clicks on submit button')
def step_impl(context):
    context.elements_attributes.click_submitBtn()

@then(u'verify that assertion result')
def step_impl(context):
    context.elements_attributes.text_box_click()
    sleep(3)

@given(u'Element Dropdown is open and clicks on Check Box Attribute')
def step_impl(context):
    context.elements_attributes = Element_Attributes_POM(context.driver)
    context.elements_attributes.check_box_navigation()


@when(u'User clicks on the Home Toggle bottom')
def step_impl(context):
    context.elements_attributes.home_toggle_Click()
