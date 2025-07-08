"""
Problem 1: Sum of Digits
Task: Take an integer as input and print the sum of its digits.
Example:
Input: 1234  
Output: 10  # (1 + 2 + 3 + 4)
source:problem taken from ChatGTP
"""
#solution
number = input("Enter a number: ")
sum=0
for i in number:
    sum+=int(i)
print(sum)

#optimal solution by chatGTP
#print("Sum of digits:", sum(int(digit) for digit in input("Enter a number: ")))