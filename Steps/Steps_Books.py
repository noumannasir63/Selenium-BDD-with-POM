from behave import *
from time import sleep
from selenium.webdriver.common.by import By
from Features.pages.POM_Books import POMBooks


@when(u'Clicks on the Books')
def step_impl(context):
    context.books_page=POMBooks(context.driver)
    context.books_page.click_books()
    sleep(3)
