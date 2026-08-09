students=[]
for i in range(5):
    name=input(f"Enter {i+1} student name: ")
    students.append(name)

for name in students:
    print(name)

for position,name in enumerate(students,start=1):
    print(position,name)

count=0
for name in students:
    if len(name) > 5:
        count += 1
print(f"{count} names contain more than five characters.")        

    
