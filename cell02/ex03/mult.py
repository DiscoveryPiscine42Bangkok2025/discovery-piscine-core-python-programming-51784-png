#!/usr/bin/env python3

# Ask for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Multiply numbers
result = num1 * num2

# Check result
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is zero.")

# Display multiplication result
print("Result:", result)