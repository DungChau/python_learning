from tree import *
from behave import *

@given('a set of specific people')
def step_create_tree(context):
	context.tree = Tree()
	for row in context.table:
		context.tree.insert(row["name"],int(row["age"]))

@then('we will find a person 45 year old')
def step_person(context):
	child , p = context.tree.search("Xie")
	assert( child.node.val == 45)
	