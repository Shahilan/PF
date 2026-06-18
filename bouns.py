salary=int(input("Enter your Salary: "))
if salary>=100000:
    bouns=salary*15/100
    print("Your Bouns is, " ,bouns)
    
elif salary>=50000 and salary<100000:
    bouns=salary*10/100
    print("Your Bouns is, " ,bouns)
else:
    bouns=salary*5/100
    print("Your Bouns is, " ,bouns)
    
