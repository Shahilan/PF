marks=[]
total=0
for i in range(5):
    m=int(input(f"Enter {i+1} subject marks: "))
    marks.append(m)
    total+=m
    avg=total/len(marks)
print(marks)
print("Total marks is: ",total)
print("Average marks is: ",avg)

x=marks[0]
for i in range(len(marks)):
    if marks[i]>x:
        x=marks[i]
print(f"{x} is highest marks")

for i in range(len(marks)):
    if marks[i]<x:
        x=marks[i]
print(f"{x} is lowest marks")

count=0
for i in range(len(marks)):
    if marks[i]<50:
        count+=1
print(f"{count} subjects have marks below 50")

if avg>=75:
    print("Grade A")
elif avg>=60:
    print("Grade B")
elif avg>=50:
    print("Grade C")
else:
    print("Grade F")




