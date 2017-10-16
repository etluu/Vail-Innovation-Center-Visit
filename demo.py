import sys
number1 = int(input("Enter your first number - "))
number2 = int(input("Enter your second number - "))
op = input("Would you like to add, subtract, multiply or divide? ")
if(op == "add"):
	print(number1+number2)
elif(op == "subtract"):
	print(number1-number2)
elif(op == "multiply"):
	print(number1*number2)
elif(op == "divide"):
	print(number1/number2)
else:
	print("Not a valid number! - Try again!")
