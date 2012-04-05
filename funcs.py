#!/usr/local/bin/python3

def get_int(msg):
	while True:
		try:
			i = int(input(msg))
			return i
		except ValueError as e:
			print(e)

age = get_int('Enter your age: ')

if age >= 18 and age <= 120:
	print('Your grownup already!')
elif age >= 0 and age < 18:
	print('Still a kid')
elif age > 120:
	print('a fairy huh!')
else:
	print('not a human!!!!')


