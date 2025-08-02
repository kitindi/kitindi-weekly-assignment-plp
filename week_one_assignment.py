# WEEK ONE ASSIGNMENT
# Basic Calculator Program
# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division)
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15

print("Welcome to the Calculator App: ")
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
result = 0

operator = input("Enter operator : +  for adding\n  or -  get difference\n or *  for multiplication\n or / for divison: ")

if operator == "+":
    result = first_number + second_number

if operator == "-":
      if first_number > second_number:
            result = first_number - second_number
      else:
          result = second_number - first_number

if operator == "*":
    result = first_number * second_number
    

if operator == "/":
    result = first_number / second_number

print("The result is : " + str(result))
    
    
    

