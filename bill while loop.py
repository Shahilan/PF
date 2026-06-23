#while
total = 0
no_of_product = 0
while True:
    bill=int(input("Enter product price(If you leave press 0): "))
    if bill == 0:
        break
    else:
        total += bill
        no_of_product += 1
print("No of Product: ",no_of_product)
print("Total Bill: ",total)



    
    
    
