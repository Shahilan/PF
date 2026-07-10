freezer=1
total_box=0
total_ice=0
while freezer<=4:
    box=1
    while box<=6:
        total_box += 1
        total_ice += 20 
        box += 1
    freezer += 1
print("Total number of ice cream boxes: ",total_box)   
print("Total number of ice creams in the shop: ",total_ice)      
