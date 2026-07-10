flight=1
one_flight=0
all_flight=0
while flight<=5:
    row=1
    one_flight=0 #reset
    while row<=30:
        seat=1
        while seat<=6:
            one_flight+=1
            all_flight+=1
            seat+=1
        row+=1
    flight+=1
print(" Number of passengers on one flight: ",one_flight)    
print(" Total number of passengers on all flights: ",all_flight)


        
