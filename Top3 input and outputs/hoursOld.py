# Calculating hours. Calculate the user’s age in hours.
# You will need to ask the user to enter a whole number here. 
# Collect it as a float in case they get contrary.

# hours = age * 365 * 24
# Print(“\nYou’re over”, hours, “hours old”)

age = input("Enter your age: ")
hours = int(age) * 365 * 24
print("You’re over, hours old: " +  str(hours)) 
