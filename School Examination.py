room=1
total_student=0
total_fee=0
while room <= 5:
    student = 1
    while student <= 25:
        total_student += 1
        total_fee += 500
        student += 1
    room += 1
print("Total number of students: ",total_student)
print("Total examination fee collected: ",total_fee)
        
    
