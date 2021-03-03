# Input two integer numbers num1 and num2 from the keyboard.
# Display the whole part and the remainder part of the result when num1 is divided by num2.

num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))

result = num1 % num2
print("result = " + str(result))