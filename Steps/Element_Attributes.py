from behave import *
from time import sleep


from Features.pages.ELement_Attributes_POM import Element_Attributes_POM

@given(u'Element Dropdown is open and clicks on Text Box Attribute')
def step_impl(context):
    context.elements_attributes = Element_Attributes_POM(context.driver)
    context.elements_attributes.text_box_click()
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


@then(u'User clicks on submit button')
def step_impl(context):
    context.elements_attributes.click_submitBtn()
