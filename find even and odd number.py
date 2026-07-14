count=1
even=0
odd=0
while count <= 5:
    num=int(input("Enter a num: "))
    if num%2 == 0:
        even += 1
    else:
        odd += 1
    count += 1 
print("Total even numbers: ",even)
print("Total odd numbers: ",odd) 
        
    
