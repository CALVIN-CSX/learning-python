"""
Problem 3: Count Vowels in a String

📘 Description:
This program takes a string input from the user and counts the number of vowels (a, e, i, o, u) in it.
It works regardless of the case (uppercase/lowercase).

🔢 Example:
Input:  Hello World
Output: 3  # (e, o, o)
Source: Problem taken from ChatGPT
"""
#solution
text=input("Enter a string/text: ").lower()
count=0
for x in text:
    if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
        count+=1
    else:
        continue

print(f"{count} vowels found in {text}")
#solution by ChatGTP
"""
text = input("Enter a string: ")
vowels = "aeiou"
count = 0

for char in text.lower():  # Convert input to lowercase to make it case-insensitive
    if char in vowels:
        count += 1

print(f"Number of vowels: {count}")
"""