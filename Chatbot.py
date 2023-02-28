#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Welcome to the Basic Math Operations Bot!")
greet=input('User:')
print(greet)
def calculate():
    try:
        num1 = float(input("Enter first operand: "))
        num2 = float(input("Enter second operand: "))
        operation = input("Enter the operation you want to perform (+, -, *, /): ")
        
        if operation == "+":
            result = num1 + num2
            print("The sum is:", result)
        elif operation == "-":
            result = num1 - num2
            print("The difference is:", result)
        elif operation == "*":
            result = num1 * num2
            print("The product is:", result)
        elif operation == "/":
            result = num1 / num2
            print("The quotient is:", result)
        else:
            print("Invalid operation selected. Please try again.")
            calculate()
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        calculate()

calculate()

while True:
    more_operations = input("Do you want to perform more operations? (yes/no): ")
    if more_operations.lower() == "yes":
        calculate()
    else:
        print("Thank you for using the Basic Math Operations Bot!")
        break


# In[ ]:




