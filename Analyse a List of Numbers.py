nums=[12, 7, 25, 7, 18, 4, 7, 30]
x=nums[0]

for no in nums:
    if no > x:
        x=no
print("Maximum: ",x)

for no in nums:
    if no < x:
        x=no
print("Minimum: ",x)

count=0
for no in nums:
    if no == 7:
        count += 1
print(f"{count} times 7 appears")

total=0
for no in nums:
    total += no
    avg = total/len(nums)
print(f"Total is {total}")
print(f"Average is {avg}")

print(nums[::-1])

for i in range(len(nums)-1,-1,-1):
    print(nums[i])








    
