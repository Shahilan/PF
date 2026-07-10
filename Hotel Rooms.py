floor=1
total_room=0
income=0
while floor<=6:
    room=1
    while room<=18:
        total_room+=1
        income+=12000
        room+=1
    floor+=1
print("Total number of rooms: ",total_room)
print("Total income for one night: ",income)
        
