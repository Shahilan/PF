distance=float(input("Enter the distance travel: "))
fuel_price=float(input("Enter the fuel price per liter: "))
fuel_economy=float(input("Enter the fuel economy (km per liter): "))
highway_fee=float(input("Enter the highway fee: "))
consumed_fuel=distance/fuel_economy
total_fuel_cost=consumed_fuel*fuel_price
total_cost=total_fuel_cost+highway_fee
print("The total fuel consumed is: ", consumed_fuel, " liters")
print("The total fuel cost is: ", total_fuel_cost)
print("The total cost of the trip is: ", total_cost) 