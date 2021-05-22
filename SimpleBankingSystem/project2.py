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

