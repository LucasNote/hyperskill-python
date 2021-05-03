
number = 476

number=int(input("Type a number:"))

sum_of_digits = 0
for digit in str(number):
    sum_of_digits += int(digit)

print(sum_of_digits)


number=int(input("number:"))
word=str(input("text"))

text=""
for x in range(0, number):
    text += word

print(text)



number=int(input("number:"))
word=str(input("text"))
print(word * number)


# 4. Boolean values
a = True
b = not a

print(not (a and b))

#6. Calculator
# 12 34 56 78 97 45 23 67
calculations = input().split()
print(calculations[-1])

#7. Carry on!
height, width, length = 4, 30, 50   # False
height, width, length = 15, 25, 37  # True
height, width, length = 25, 30, 23  # True
height, width, length = 10, 35, 35  # True
allowed = (height <= 10 < width <= 35 < length <= 40) or (height + width + length <= 80)
print(allowed)


#10. To infinity and beyond
number = 5
# while number > 0:             # loop
# while number*2 < 1000:
# while number % 100 != 1:      # loop
while True:
    print(number)
    number += 1


# Work on project. Stage 1/4: Rush into print.
print("I love animals!")
print("Let's check on the animals...")
print("The deer looks fine.")
print("The bat looks happy.")
print("The lion looks healthy.")

# What you'll do in this stage 2/4: Show me an animal!
camel = (r"""Switching on the camera in the camel habitat...
___.-''''-.
/___  @    |
',,,,.     |         _.'''''''._
     '     |        /           \
     |     \    _.-'             \
     |      '.-'                  '-.
     |                               ',
     |                                '',
      ',,-,                           ':;
           ',,| ;,,                 ,' ;;
              ! ; !'',,,',',,,,'!  ;   ;:
             : ;  ! !       ! ! ;  ;   :;
             ; ;   ! !      ! !  ; ;   ;,
            ; ;    ! !     ! !   ; ;
            ; ;    ! !    ! !     ; ;
           ;,,      !,!   !,!     ;,;
           /_I      L_I   L_I     /_I
Look at that! Our little camel is sunbathing!""")
print(camel)

# What you'll do in this stage 2/4: Show me an animal!
camel = ("Switching on the camera in the camel habitat...\n"
         "___.-''''-.\n"
         "/___  @    |\n"
         "',,,,.     |         _.'''''''._\n"
         "     '     |        /           \\n"
         "     |     \    _.-'             \\n"
         "     |      '.-'                  '-.\n"
         "     |                               ',\n"
         "     |                                '',\n"
         "      ',,-,                           ':;\n"
         "           ',,| ;,,                 ,' ;;\n"
         "              ! ; !'',,,',',,,,'!  ;   ;:\n"
         "             : ;  ! !       ! ! ;  ;   :;\n"
         "             ; ;   ! !      ! !  ; ;   ;,\n"
         "            ; ;    ! !     ! !   ; ;\n"
         "            ; ;    ! !    ! !     ; ;\n"
         "           ;,,      !,!   !,!     ;,;\n"
         "           /_I      L_I   L_I     /_I\n"
         "Look at that! Our little camel is sunbathing!")

print(camel)


# example 1
print("You're doing great!")
print('You\'re doing great!')
# example 2
print("Have you read \"Hamlet\"?")
print('Have you read "Hamlet"?')

# Multiline strings
print("""This
is
a
multi-line
string""")

print('''This
is
a
multi-line
string''')

# PEP 8 Test
print('Always write beautiful code!')

print("line 1")
# print("line 2")
print("line 3")  # print("line 4")

# create a variable x
# with the value 8
x = 8
x = x * x
print(x)  # prints the x squared

word = word.replace("\u0301", "")  # delete stress symbols from the word
print(word)


# print('that's cool')
print("some 'boring' string")
# print('letter \'q\' is my favourite"'")
print("these are my friend's cats")
# print("\"canoodle" is a real word!") \

print("' '' '''")
print("' '' '''")
print("' '' '''")

print("""' '' '''
' '' '''
' '' '''""")


print('Did that stop the old Grinch?')
print('No! The Grinch simply said,')
print('"If I can\'t find a reindeer,')
print('I\'ll make one instead!"')

print("""Did that stop the old Grinch?
No! The Grinch simply said,
"If I can't find a reindeer,
I'll make one instead!"
""")

print("""'
'"'
'"'"'
'"'"'"'""")


print(r"""
Switching on the camera in the camel habitat...
 ___.-''''-.
/___  @    |
',,,,.     |         _.'''''''._
     '     |        /           \
     |     \    _.-'             \
     |      '.-'                  '-.
     |                               ',
     |                                '',
      ',,-,                           ':;
           ',,| ;,,                 ,' ;;
              ! ; !'',,,',',,,,'!  ;   ;:
             : ;  ! !       ! ! ;  ;   :;
             ; ;   ! !      ! !  ; ;   ;,
            ; ;    ! !     ! !   ; ;
            ; ;    ! !    ! !     ; ;
           ;,,      !,!   !,!     ;,;
           /_I      L_I   L_I     /_I
Look at that! Our little camel is sunbathing!""")

camel = r"""Switching on the camera in the camel habitat...
 ___.-''''-.
/___  @    |
',,,,.     |         _.'''''''._
     '     |        /           \
     |     \    _.-'             \
     |      '.-'                  '-.
     |                               ',
     |                                '',
      ',,-,                           ':;
           ',,| ;,,                 ,' ;;
              ! ; !'',,,',',,,,'!  ;   ;:
             : ;  ! !       ! ! ;  ;   :;
             ; ;   ! !      ! !  ; ;   ;,
            ; ;    ! !     ! !   ; ;
            ; ;    ! !    ! !     ; ;
           ;,,      !,!   !,!     ;,;
           /_I      L_I   L_I     /_I
Look at that! Our little camel is sunbathing!"""
print(camel)


times, word = input("Enter a two value: ").split()
print(str(word) * int(times))

times = int(input())
word = str(input())
print(word * times)

# Taking input  Sum of two floats
var_float1 = float(input())
var_float2 = float(input())
print(var_float1 + var_float2)

# Taking input -> Hello!
template = "Hello, "
input_text = input()
print(template + input_text)

# 4.4
# Program with numbers > The sum of digits
number = input()

sum_of_digits = 0
# for digit in str(number):
for digit in number:
    print(digit)
    # sum_of_digits += int(digit)

print(sum_of_digits)

# Program with numbers > Divide nuts equally between squirrels
n = int(input())
k = int(input())
print(int(k / n))

# Program with numbers > Good rest on vacation
days = int(input())
food_per_day = int(input())
flight = int(input())
hotel_per_day = int(input())
night = days - 1

total = (food_per_day * days) + (flight * 2) + (hotel_per_day * night)
print(total)

# Ref code
duration_day = int(input())
food_cost_per_day = int(input())
one_way_flight_cost = int(input())
cost_of_one_night = int(input())
total_food_cost = food_cost_per_day * duration_day
total_night = duration_day - 1
total_night_cost = total_night * cost_of_one_night
sum_total = total_food_cost + total_night_cost + one_way_flight_cost * 2
print(sum_total)

# Comparisons > Focus on the positive
a = int(input().strip())
print(a > 0)

# If statement > The minimum
a, b = 2, 1
minimum = a
if b < minimum:
    minimum = b

print(minimum)

# While loop > Follow the "i"
i = 0
while i <= 10:
    i = i + 1
    if i > 7:
        # print(f"here {i}")
        i = i + 2
print(i)


# Starting with GitHub > Registration on GitHub
# https://github.com/LucasNote

# Starting with GitHub > Find a repo on GitHub
# https://github.com/LucasNote/hyperskill-python

# Type casting > Casting to floats
float(-52)
float("2.x")
float("52")
float("52.0")
float(52.0)










