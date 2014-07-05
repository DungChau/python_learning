Feature: Create a binary tree of people names and ages
	Scenario: Set up the tree
		Given a set of specific people
			| name 		| age 	|
			| John		| 14	|
			| Jane		| 34	|
			| Xie		| 45	|
			| Jane		| 24 	|
		Then we will find a person 45 year old