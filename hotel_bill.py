room_charge=float(input("Enter the room charge per day: "))
number_of_days=int(input("Enter the number of days: "))
total_room_charge=room_charge*number_of_days
food_charge=float(input("Enter the food charge per day: "))
total_food_charge=food_charge*number_of_days
service_charge=float(input("Enter the service charge: "))
total_bill=total_room_charge+ total_food_charge+service_charge
sub_total=total_room_charge+total_food_charge
print("service charge: Rs", service_charge)
print("Sub total: Rs", sub_total)
print("Total bill: Rs", total_bill)
