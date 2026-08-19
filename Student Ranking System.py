details=[]
subject1=[]
subject2=[]
subject3=[]
for i in range(3):
    name=input(f"Enter {i+1} student name: ")
    details.append(name)
    mark1=int(input("Enter your first subject marks: "))
    subject1.append(mark1)
    mark2=int(input("Enter your second subject marks: "))
    subject2.append(mark2)
    mark3=int(input("Enter your third subject marks: "))
    subject3.append(mark3)

total=[]
for i in range(len(details)):
    total.append(subject1[i]+subject2[i]+subject3[i])
    
avg=[]
for i in range(len(total)):
    avg.append(total[i]/len(total))
    
for i in range(len(details)):
    print(details[i],"| Total:",total[i],"| Average:",avg[i])
print(details)
print(subject1)
print(subject2)
print(subject3) 

