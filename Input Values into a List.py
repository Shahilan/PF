numbers=[]
count=1
while count<=5:
    integer=int(input(f"Enter your {count} number: "))
    numbers.append(integer)
    count += 1   
print(numbers)
print("total: ",sum(numbers))
print("Average: ",sum(numbers)/len(numbers) )


numbers=[]
for i in range(5):
    integer=int(input(f"Enter your {i+1} number: "))
    numbers.append(integer)   
print(numbers)
print("total: ",sum(numbers))
print("Average: ",sum(numbers)/len(numbers))
