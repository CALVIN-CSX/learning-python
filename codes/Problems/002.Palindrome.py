"""
Problem 2: Palindrome Checker
Task: Take a string as input and check if it's a palindrome (reads the same forward and backward).

Example:
Input: madam
Output: Yes, it's a palindrome

Source: Problem taken from ChatGPT
"""
#solution
name = input("Enter your name: ")
print("checking if your name is palindrome...")
if name==name[::-1]:#slicing the name
    print("Yes, it's a palindrome")
else:
    print("No, it's a palindrome")

#solution by ChatGTP:
"""
# Taking user input
text = input("Enter a word or phrase: ")

# Preprocessing: removing spaces and converting to lowercase for accurate checking
processed_text = text.replace(" ", "").lower()

# Checking if the processed text is the same when reversed
if processed_text == processed_text[::-1]:
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")
"""