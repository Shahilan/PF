total = 0
for i  in range(0,5):
    unit=int(input("Enter unit: "))

    if unit <= 100:
        bill=unit*10
        
    elif unit <= 200:
        bill=(unit-100)*15 + (100*10)
            
    else:
        bill=(unit-200)*20 + (100*10) + (100*15)
    total = total + bill
    print("Your bill is" , bill)
    
print("total bill is" , total)

