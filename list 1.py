p_type=[]
p_size=[]
p_price=[]
index=0
while index < 5:
    pack_type=input(f"Enter package type {index}: ")
    p_type.append(pack_type)
    pack_size=input("Enter package size: ")
    p_size.append(pack_size)
    pack_price=int(input("Enter package price: "))
    p_price.append(pack_price)
    index += 1
print(f"{'package type' :<15}{'package size' :<15}{'package price' :<15}")
print("_"*50)
for i in range (5):
    print(f"{p_type[i] :<15}{p_size[i] :<15}{p_price[i] :<15}")
    
    
                   
     
