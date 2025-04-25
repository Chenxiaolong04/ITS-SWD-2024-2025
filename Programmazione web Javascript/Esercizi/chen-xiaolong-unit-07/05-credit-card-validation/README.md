# 05-credit-card-validation

Author: Chen Xiaolong  
Contact: xiao.chen@edu-its.it

## Exercise Requirements

Create a function `validateCreditCard` to validate a credit card number based on the following criteria:

1. The card number length must be exactly 16 characters.
2. The card number must consist only of digits (0-9).
3. The card number must not be composed of the same digit repeated.
4. The last digit of the card number must be even.
5. The sum of the digits must be greater than 16.

## Approach to Solution

### Steps:

1. **Clean the Input**: Remove dashes from the credit card number to ensure uniformity.
2. **Check Length**: Ensure that the length of the cleaned card number is exactly 16.
3. **Check for Non-Digit Characters**: Ensure that every character in the card number is a digit (0-9).
4. **Check for Repeated Digits**: Ensure that at least two different digits are present in the card number.
5. **Check Last Digit**: Ensure that the last digit of the card number is even.
6. **Check Sum**: Ensure that the sum of all the digits in the card number is greater than 16.

### Function:

The function `validateCreditCard(cardNumber)` is implemented to perform the above checks and return a result.

