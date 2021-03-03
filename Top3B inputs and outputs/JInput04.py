#Input04.py
#Input two real numbers (doubles) from the keyboard and display the difference (subtract)
# of the two numbers.

#e.g. 4 -1 = 3

#Multiply each number by 3 and again write the difference, with an appropriate message.
#e.g. After both numbers are multiplied by 3:

#3a – 3b = result, or 12-3=9



num1 = int(input("add a number: "))
num2 = int(input("add a number: "))

total = num1 - num2
print("total: " + str(total))

Newtotal = num1*3 - num2*3
print("Newtotal: " + str(Newtotal))


