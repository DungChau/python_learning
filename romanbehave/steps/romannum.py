from behave import *
from converter import *

@given('number {number} is entered to the program')
def step_enter_number(context, number):
	context.number = int(number)

@when('pass to int_to_roman')
def step_pass_to(context):
	context.result = int_to_roman(context.number)

@then('it should return "{roman}"')
def step_should_be(context, roman):
	assert(context.result == roman)