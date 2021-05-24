
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


orginal_number =                    '4000008449433403'
drop_the_last_digit =               '400000844943340'
multiply_odd_digits_by_2 =          '800000(16)48983640'
subtract_9_from_numbers_over_9 =    '800000748983640'
add_all_numbers =                   '800000748983643'


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
sum_card_number = sum(card_number_list)
print(sum_card_number)


# To find the checksum, it is necessary to find the control number for 400000844943340 by the Luhn algorithm.
# It equals 57 (from the example above). The final check digit of the generated map is 57+X, where X is checksum.
# In order for the final card number to pass the validity check, the check number must be a multiple of 10,
# so 57+X must be a multiple of 10. The only number that satisfies this condition is 3.
def get_checksum(sum_card_number):
    first_digit = int(str(sum_card_number)[-1])
    check_sum = 10 - first_digit

    return check_sum

first_digit = get_checksum(sum_card_number)
first_digit



# Two ways, 1: subtract 10 - the first digit, 2: adding 1 and check dividend is 0
first_digit = int(str(sum_card_number)[-1])
check_sum = 10 - first_digit
check_sum





# for loop with index
colors = ["red", "green", "blue", "purple"]
for i in range(len(colors)):
    print(colors[i])

# enumerate
presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for num, name in enumerate(presidents, start=0):
    print("President {}: {}".format(num, name))


# git commit -m "Simple Banking System #2 - 3, 20210522, Mac_2018", failed


# Python code to demonstrate the working of
# sum()
numbers = [1, 2, 3, 4, 5, 1, 4, 5]

# start parameter is not provided
Sum = sum(numbers)
print(Sum)

# start = 10
Sum = sum(numbers, 10)
print(Sum)

Sum = sum(card_number_list)
print(Sum)

