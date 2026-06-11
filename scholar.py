mark = int(input("Enter your marks: "))
if mark >= 75:
    income = int(input("Enter your income: "))
    if income <= 50000:
        print("scholarship apporved")
    else:
        print("not appproved")
else:
    print("marks not enough")
        
