# enter your weight in kgs: 70
# enter your height in metrtes: 1.8
# your BMI IS 21.604938271604937

weight = int(input("Enter your Weight : "))
height = float(input("Enter your Height : "))
total = int(weight) / (float(height) * float(height)) 
print(total)