# Write a program that converts Farenheit to Celsius.  Please use variables as well as the proper variable types for maximum points.
# The first prompt should be a Farenheit to Celsius.
# The second prompt should be Celsius to Farenheit.



# Program to Convert Celsius To Fahrenheit

celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))

# Program to Convert Fahrenheit to Celsius

fahrenheit = float(input("Enter temperature in fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))