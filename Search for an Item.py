course=["computing","business","bio","maths","law","management"]
name=input("what course you want: ")
for i  in course:
    if i==name.lower():  #if you want you give lowercase to i also
        print("Course Available")
        break
else:    
    print("Course Not Found")



if name.lower() in course:
    print("Course is available")
else:
    print("Course is not available")




if name.lower() in [c.lower() for c in course]:
    print("Course is available")
else:
    print("Course is not available")    
