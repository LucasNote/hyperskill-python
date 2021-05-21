# Luhn algorithm
"""
The main purpose of the check digit is to verify that the card number is valid.
Say you're buying something online, and you type in your credit card number incorrectly
by accidentally swapping two digits, which is one of the most common errors.
When the website looks at the number you've entered and applies the Luhn algorithm to the first 15 digits,
the result won't match the 16th digit on the number you entered. The computer knows the number is invalid,
and it knows the number will be rejected if it tries to submit the purchase for approval.

Another purpose of the check digit is to catch clumsy attempts to create fake credit card numbers.

Luhn Algorithm in action
The Luhn algorithm is used to validate a credit card number or other identifying numbers,
such as Social Security. The Luhn algorithm, also called the Luhn formula or modulus 10,
checks the sum of the digits in the card number and checks whether the sum matches the expected result
or if there is an error in the number sequence. After working through the algorithm,
if the total modulus 10 equals zero, then the number is valid according to the Luhn method.

If the received number is divisible by 10 with the remainder equal to zero, then this number is valid;
otherwise, the card number is not valid. When registering in your banking system,
you should generate cards with numbers that are checked by the Luhn algorithm.
You know how to check the card for validity.

First, we need to generate an Account Identifier, which is unique to each card.
Then we need to assign the Account Identifier to our BIN (Bank Identification Number).
As a result, we get a 15-digit number 400000844943340, so we only have to generate the last digit,
which is a checksum.

To find the checksum, it is necessary to find the control number for 400000844943340 by the Luhn algorithm.
It equals 57 (from the example above). The final check digit of the generated map is 57+X,
where X is checksum. In order for the final card number to pass the validity check,
the check number must be a multiple of 10, so 57+X must be a multiple of 10.
The only number that satisfies this condition is 3.

Therefore, the checksum is 3. So the total number of the generated card is 4000008449433403.
The received card is checked by the Luhn algorithm.

You need to change the credit card generation algorithm so that they pass the Luhn algorithm.
"""

# value= '400000844943340'
# 4 + 8 + 4 + 4 + 9 + 4 + 3 + 3 + 4
orginal_number =                    '4000008449433403'
drop_the_last_digit =               '400000844943340'
multiply_odd_digits_by_2 =          '800000(16)48983640'
subtract_9_from_numbers_over_9 =    '800000748983640'
add_all_numbers =                   '800000748983643'

sum = 0
for v in orginal_number:
    if v.isdigit():
        sum += int(v)
print(sum)

# not working
# total = sum(map(int, filter(str.isdigit, value.split())))
# print(total)

def sum_digits_string(str1):
    sum_digit = 0
    for x in str1:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z

    return sum_digit

sum2 = sum_digits_string(orginal_number)
print('orginal_number', sum_digits_string(orginal_number))
print('subtract_9_from_numbers_over_9', sum_digits_string(subtract_9_from_numbers_over_9))
print('add_all_numbers', sum_digits_string(add_all_numbers))

# Convert string digits to a int list
card_number_list = list(map(int, str(orginal_number)))
print(card_number_list)

# Convert list to string
listToStr = ''.join(map(str, card_number_list))
print(str(listToStr))


# org_num_list = list(str(orginal_number))
# org_num_list_int = list(map(int, org_num_list))
# print(org_num_list)
# print(org_num_list_int)


# [Convert number to list of integers]
# initializing number
num = 2019

# printing number
print ("The original number is " + str(num))

# using list comprehension
# to convert number to list of integers
res = [int(x) for x in str(num)]

# printing result
print ("The list from number is " + str(res))


# Python program to convert a list
# to string using list comprehension
s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']

# using list comprehension
listToStr = ' '.join(map(str, s))

print(listToStr)


# orginal_number =                    '4000008449433403'
# drop_the_last_digit =               '400000844943340'
# multiply_odd_digits_by_2 =          '800000(16)48983640'
# subtract_9_from_numbers_over_9 =    '800000748983640'
# add_all_numbers =                   '800000748983643'

# 1. Convert str to a list with int
card_number_list = list(map(int, str(orginal_number)))
print(card_number_list)

# 2. Drop the last digit
card_number_list = card_number_list[:-1]
print(card_number_list)

# 3. Multiply odd digits by 2
# [8, 0, 0, 0, 0, 0, 16, 4, 8, 9, 8, 3, 6, 4, 0]
for a in range(1, len(card_number_list) + 1, 2):
    print(a, card_number_list[a - 1], card_number_list[a - 1] * 2)
    card_number_list[a - 1] *= 2

# 4. Subtract 9 from numbers over 9
# [8, 0, 0, 0, 0, 0, 7, 4, 8, 9, 8, 3, 6, 4, 0]
def subtract9_over9(lst):
    for idx, val in enumerate(lst):
        if val > 9:
            print(idx, val)
            card_number_list[idx] -= 9

subtract9_over9(card_number_list)
print(card_number_list)

# 5. Add all numbers


# for loop with index
colors = ["red", "green", "blue", "purple"]
for i in range(len(colors)):
    print(colors[i])

# enumerate
presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for num, name in enumerate(presidents, start=0):
    print("President {}: {}".format(num, name))


