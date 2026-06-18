weight=int(input("Enter your Wieght: "))
if weight<=20:
    print("No Charge")
elif weight<=30:
    charge=(30-20)*200
    print("Charge is " ,charge)
else:
        print("Not Allowed")
