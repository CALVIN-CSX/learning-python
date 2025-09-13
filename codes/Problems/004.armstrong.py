"""
Problem 4: Armstrong Number Checker

📘 Description:
This program takes an integer as input and checks if it's an Armstrong number.
An Armstrong number (also known as a narcissistic number) is a number that is equal to 
the sum of its own digits each raised to the power of the number of digits.

🔢 Example:
Input:  153
Output: Armstrong number  # (1³ + 5³ + 3³ = 1 + 125 + 27 = 153)

Input:  123
Output: Not Armstrong number  # (1³ + 2³ + 3³ = 1 + 8 + 27 = 36 ≠ 123)

Source: Problem taken from ChatGPT
"""

# Original solution
n = int(input("enter the number"))
sum = 0
digits = list(str(n))
for digit in digits:
    sum = sum + (int(digit) ** (len(digits)))
if n == sum:
    print("Armstrong number")
else:
    print("Not Armstrong number")

# Alternative solution approach:
"""
n = int(input("Enter a number: "))
digits = str(n)
num_digits = len(digits)
sum_of_powers = sum(int(digit) ** num_digits for digit in digits)

if n == sum_of_powers:
    print("Armstrong number")
else:
    print("Not Armstrong number")
"""