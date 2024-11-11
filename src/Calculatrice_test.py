#Name: Calculatrice
#Author: Imad
#Date: 07.11.2024

"""Les fonctions"""

def add (x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

operator = input("Enter operator: ")
if operator == "+":
    print(first_number + second_number)
elif operator == "-":
    print(first_number - second_number)
elif operator == "*":
    print(first_number * second_number)
else:
    if second_number == 0:
        print("Opreation Impossible")
    else:
        print(first_number / second_number)

