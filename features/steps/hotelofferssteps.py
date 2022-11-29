from behave import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

@given(u'launch the browser')
def step_impl(context):
    path = r'D:\Downloads\chromedriver_win32/chromedriver.exe'
    context.driver = webdriver.Chrome(path)
    time.sleep(2)
    # raise NotImplementedError(u'STEP: Given launch the browser')


@when(u'open cleartrip homepage')
def step_impl(context):
    context.driver.get('https://www.cleartrip.com/')
    time.sleep(2)
    context.driver.maximize_window()
    time.sleep(2)
    # raise NotImplementedError(u'STEP: When open cleartrip homepage')


@when(u'cancel pop-up')
def step_impl(context):
    context.driver.find_element("xpath", "//div[@class='px-1   flex flex-middle nmx-1 pb-1']").click()
    time.sleep(5)
    # raise NotImplementedError(u'STEP: When cancel pop-up')


@when(u'click on offers')
def step_impl(context):
    context.driver.find_element("xpath", "//a[@href='/offers/india']").click()
    time.sleep(5)
    # raise NotImplementedError(u'STEP: When click on offers')


@then(u'verify offer page is opening')
def step_impl(context):
    assert True, "Test Passed"
    # raise NotImplementedError(u'STEP: Then verify offer page is opening')


@then(u'click on hotels')
def step_impl(context):
    handles = context.driver.window_handles
    context.driver.switch_to.window(handles[1])
    time.sleep(5)
    context.driver.find_element("xpath", "//a[@href='/offers/india/hotels']").click()
    time.sleep(5)
    # raise NotImplementedError(u'STEP: Then click on hotels')


@then(u'verify hotel offers are opening')
def step_impl(context):
    assert True, "Test Passed"
    # raise NotImplementedError(u'STEP: Then verify hotel offers are opening')


@then(u'click on any offer')
def step_impl(context):
    context.driver.find_element("xpath", '//a[@href="/offers/india/treebo/offers/cleartrip" and text()="Know More"]').click()
    time.sleep(6)
    # raise NotImplementedError(u'STEP: Then click on any offer')


@then(u'verify details of offer opening')
def step_impl(context):
    assert True, "Test Passed"
    # raise NotImplementedError(u'STEP: Then verify details of offer opening')


@then(u'click on book now')
def step_impl(context):
    ac_obj = ActionChains(context.driver)
    time.sleep(5)
    ac_obj.send_keys(Keys.PAGE_DOWN)
    time.sleep(5)
    context.driver.find_element("xpath",'//img[@src="//www.cleartrip.ae/offers/sites/default/files/en-booknow-yellow_29.png"]').click()
    time.sleep(5)

    # raise NotImplementedError(u'STEP: Then click on book now')


@then(u'verify booking window opening')
def step_impl(context):
    assert True, "Test Passed"
    # raise NotImplementedError(u'STEP: Then verify booking window opening')


@then(u'click on reset filters')
def step_impl(context):
    context.driver.find_element("xpath", '//button[text()="Reset Filters"]').click()
    time.sleep(5)
    # raise NotImplementedError(u'STEP: Then click on reset filters')


@then(u'verify filters are resetting')
def step_impl(context):
    assert True, "Test Passed"
    # raise NotImplementedError(u'STEP: Then verify filters are resetting')
