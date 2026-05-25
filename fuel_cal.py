distance_travelled=float(input("Enter the distance travelled in km: "))
fuel_efficiency=float(input("Enter the fuel efficiency in km/l: "))
fuel_price=float(input("Enter the fuel price in per liter: "))
highway_charge=float(input("Enter the highway charge in per liter: "))
fuel_consumed=distance_travelled/fuel_efficiency
total_fuel_cost=fuel_consumed*fuel_price
total_cost=total_fuel_cost+highway_charge
print("Fuel consumed: ", fuel_consumed)
print("Total fuel cost: ", total_fuel_cost)
print("Total cost: ", total_cost)