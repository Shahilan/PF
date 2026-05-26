item_1 = float(input("Enter the price per unit: Rs "))
item_2 = float(input("Enter the price per unit: Rs "))
item_3 = float(input("Enter the price per unit: Rs "))
quantity_item_1 = int(input("Enter quantity: "))
quantity_item_2 = int(input("Enter quantity: "))
quantity_item_3 = int(input("Enter quantity: "))
total_price = (item_1 * quantity_item_1) + (item_2 * quantity_item_2) + (item_3 * quantity_item_3) + 5.0
print("Delivery fee: Rs 5.0 ")
print("Total price: Rs " , total_price)
discount = total_price * 0.1 
print("Discount: Rs" , discount)
final_price = total_price - discount
print("Final price to pay: Rs " , final_price)
