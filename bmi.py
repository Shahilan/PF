weight=float(input("Enter the weight: "))
height=float(input("Enter the height: "))
bmi=weight/(height**2)
print("The BMI is: ", bmi)
if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal weight")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
else:
    print("Obese")