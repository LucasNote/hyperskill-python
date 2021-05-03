"""
About
Everything goes digital these days, and so does money. Today, most people have credit cards,
which save us time, energy and nerves. From not having to carry a wallet full of cash to consumer protection,
cards make our lives easier in many ways. In this project, you will develop a simple banking system with database.

Learning outcomes
In this project, you will find out how the banking system works and learn about SQL.
We'll also see how Luhn algorithm can help us avoid mistakes when entering the card number.
As an overall result, you'll get new experience in Python.

Description: https://hyperskill.org/projects/109/stages/591/preview

"""


# 4/1: Card anatomy
# Theory: String formatting
print(11 / 3)  # 3.6666666666666665
print('%.3f' % (11/3))  # 3.667
print('%.2f' % (11/3))  # 3.67

# 1. The str. format() method
# The operation of the method is already described in its name: in the string part,
# we introduce curly braces as placeholders for variables enlisted in the format part:
print('Mix {}, {} and a {} to make an ideal omelet.'.format('2 eggs', '30 g of milk', 'pinch of salt'))
print('{0} in the {1} by Frank Sinatra'.format('Strangers', 'Night'))
print('{1} in the {0} by Frank Sinatra'.format('Strangers', 'Night'))

# We can also use keywords to make such strings more readable. Don't forget that you can easily break the lines!
print('The {film} at {theatre} was {adjective}!'.format(film='Lord of the Rings',
                                                        adjective='incredible',
                                                        theatre='BFI IMAX'))

# Also, you can combine both positional and keyword arguments:
print('The {0} was {adjective}!'.format('Lord of the Rings', adjective='incredible'))
# The Lord of the Rings was incredible!

# Keep tabs on the order of your arguments, though:
# print('The {0} was {adjective}!'.format(adjective='incredible', 'Lord of the Rings'))
# SyntaxError: positional argument follows keyword argument

"""
Formatted string literals
Formatted string literals (or, simply, f-strings) are used to embed the values of expressions  
inside string literals. This way is supposed to be the easiest one: you only need to put f before the string 
and put the variables you want to embed into the string in curly braces. 
They are also the newest feature among all string formatting methods in Python.
"""
name = 'Elizabeth II'
title = 'Queen of the United Kingdom and the other Commonwealth realms'
reign = 'the longest-lived and longest-reigning British monarch'
f'{name}, the {title}, is {reign}.'
print(f'{name}, the {title}, is {reign}.')


hundred_percent_number = 1823
needed_percent = 16
needed_percent_number = hundred_percent_number * needed_percent / 100

print(f'{needed_percent}% from {hundred_percent_number} is {needed_percent_number}')
# 16% from 1823 is 291.68

print(f'Rounding {needed_percent_number} to 1 decimal place is {needed_percent_number:.1f}')
# Rounding 291.68 to 1 decimal place is 291.7


# 6.1.3.1. Format Specification Mini-Language¶
# https://docs.python.org/3.6/library/string.html#format-specification-mini-language

# String formatting > Divide
'%.5f' % (100/6)
'{1} divided by {0} equals {2}'.format(6, 100, 100/6)
'{} divided by {} equals {:.5f}'.format(100, 6, 100/6)
'{dividend} / {divisor} = {quotient}'.format(quotient=100/6, divisor=6, dividend=100)

# String formatting > Correct format
# print('%.3f' % (11/3))  # 3.667
"%.4f".format(3.14159265358979)
"{1} {1} {1}".format(1, 2, 3)
# "{1} is a {kind}".format(kind="fruit", "grapefruit")  # SyntaxError: positional argument follows keyword argument
"{city} is the capital of {country}".format(country="Portugal",
                                            city="Lisbon")

# String formatting > Write a number:
print('%.2f' % (21/4))

# String formatting > Film
