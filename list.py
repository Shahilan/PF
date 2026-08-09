#Question1
animal=["Dog","Cat","Lion","Husky","Rabbit"]
print(animal)
print(animal[0])
print(len(animal))

#negative indexing
print(animal[-1])

#slicing
print(animal[2:4])

#[start:end:step]
print(animal[::-1])
print(animal[0:5:2])
print(animal[::2])

#Question2
colors=["red","blue","green"]
print(colors)
colors.append("yellow")
print(colors)
colors.insert(1,"pink")
print(colors)
colors.remove("blue")
print(colors)

#Question3
numbers=[]
for i in range(5):
    num = int(input(f"Enter {i+1} number:"))
    numbers.append(num)
    tot=sum(numbers)
    avg=tot/len(numbers)
print(numbers)
print("Total is: ",tot)
print("Average is: ",avg)

#Question4
students=[]
for i in range(5):
    num = int(input(f"Enter {i+1} student name: "))
    numbers.append(students)

for student in students:
    print(student)








































































