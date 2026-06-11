salary=int(input("Enter your Salary: "))
if salary >= 50000:
    credit = int(input("Enter your credit: "))
    if credit >= 700:
        print("Approved")
    else:
        print("Credit not enough")
else:
    print("salary not enough")
