# Write a program that converts miles to kilometres. 
# (There is approximately 5/8 of a mile in one kilometre)
# Include an input that collects the number of miles from the user- as a float, 
# then displays the result of the conversion with a statement.
# The result may be expressed as a float also.
# Sample output could be:

# Enter number of miles: 60
# 60.0 miles = 96.0 kilometres 


miles = input("number of mile: ")
kilomiters = int(miles) * 8/5
print (str(kilomiters) + " kilomoters")