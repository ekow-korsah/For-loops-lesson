# Write a Python program that checks the grades of students in a class and assigns them a letter grade based on the
# following criteria:
#
# A: 90 and above
# B: 80 to 89
# C: 70 to 79
# D: 60 to 69
# F: Below 60
# The program should take an integer input representing the student's grade and output the corresponding letter grade.
# Input: student's grade
# grade = int(input("Enter the student's grade: "))
#
# # Determine the letter grade using if-elif-else statements
# if grade >= 90:
#     letter_grade = 'A'
# elif grade >= 80:
#     letter_grade = 'B'
# elif grade >= 70:
#     letter_grade = 'C'
# elif grade >= 60:
#     letter_grade = 'D'
# else:
#     letter_grade = 'F'
#
# # Output the letter grade
# print(f"The student's letter grade is: {letter_grade}")
#


#
# Write a Python program that asks the user to input the current temperature in Celsius. The program should then determine the appropriate clothing recommendation based on the following temperature ranges:
#
# Below 0°C: "Wear a heavy coat, gloves, and a scarf."
# 0°C to 10°C: "Wear a coat and a hat."
# 11°C to 20°C: "Wear a light jacket or sweater."
# 21°C to 30°C: "Wear a t-shirt and shorts."
# Above 30°C: "Wear light clothing and stay hydrated."
# If the input temperature is exactly 20°C, the program should also print, "It's a perfect day!"

# Input: temperature in Celsius
temperature = float(input("Enter the current temperature in Celsius: "))

# Determine clothing recommendation
if temperature < 0:
    recommendation = "Wear a heavy coat, gloves, and a scarf."
elif temperature <= 10:
    recommendation = "Wear a coat and a hat."
elif temperature <= 20:
    recommendation = "Wear a light jacket or sweater."
    if temperature == 20:
        recommendation += " It's a perfect day!"
elif temperature <= 30:
    recommendation = "Wear a t-shirt and shorts."
else:
    recommendation = "Wear light clothing and stay hydrated."

# Output the recommendation
print(recommendation)






# Example 1: Print the first 10 natural numbers using for loop.

# for i in range(1,11):
#     print(i)

# Example 2: Python program to print all the even numbers within the given range.

# ranges = 50
# for i in range(1, ranges):
#     if i % 2 == 0:
#         print(i)

# Example 3: Python program to calculate the sum of all numbers from 1 to a given number.

# number = 10
# total = 0
#
# for i in range(number):
#     current = i+1
#     total = total + current
#
# print(total)

# Example 4: Python program to calculate the sum of all the odd numbers within the given range.

# number = 10
# total = 0
#
# for i in range(number):
#     if i % 2 != 0:
#         total = total + i
#
# print(total)

# Example 5: Python program to print a multiplication table of a given number

# number = 5
# table_limit = 13
#
# for i in range(table_limit):
#     print(number, "x", i, "=", number * i)

# Example 6: Python program to display numbers from a list using a for loop.

# lists = [1, 2, 4, 6, 88, 125]
# for i in lists:
#     print(i)

# Example 7: Python program to count the total number of digits in a number.

# number = 1232421
# counter = 0
# convertor = str(number)
# for i in convertor:
#     counter += 1
#
# print(counter)


# Example 8: Python program to check if the given string is a palindrome.
# word = "happy"
# reverse_word = ""
# for i in word:
#     reverse_word = i + reverse_word
#
# print(reverse_word)
# if word == reverse_word:
#     print("This word is a palindrome")
# else:
#     print("This word is not a palindrome")

