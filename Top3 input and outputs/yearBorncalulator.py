# Expand the code below, so that you can collect an input from the user to work out their
#  year of birth if you collect their current age. Collect the age as a float. 
# Express the year born as an integer. Save as yearBornCalculator.py 

# collect age input from user 

age = int(input("enter your age: "))
print("your age is {0}".format(age))

yearBorn = 2021 - age
print("your age is {0} and your were born in {1} ".format(age,yearBorn))
