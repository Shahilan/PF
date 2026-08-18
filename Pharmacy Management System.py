code = [
    "MED001", "MED002", "MED003", "MED004", "MED005",
    "MED006", "MED007", "MED008", "MED009", "MED010"
]

name = [
    "Paracetamol", "Vitamin C", "Cough Syrup", "Antacid",
    "Pain Relief Gel", "Face Mask Pack", "Hand Sanitizer",
    "Bandage Roll", "Antibiotic Cream", "Digital Thermometer"
]

price = [
    120.00, 450.00, 780.00, 350.00, 920.00,
    180.00, 520.00, 250.00, 680.00, 2150.00
]

sold_code = []
sold_name = []
sold_qty = []
sold_price = []
sold_total = []
total=0
choice=int(input("Enter 1 for bill counter or enter 0 to exit: "))
while choice != 0:
    medi_code=input("Enter medicine code: ")
    qty=int(input("Enter medicine quantity: "))

    for i in range(len(code)):
        if code[i] == medi_code:
            total += price[i]*qty
            sold_code.append(code[i])
            sold_name.append(name[i])
            sold_qty.append(qty)
            sold_price.append(price[i])
            sold_total.append(price[i] * qty)
    choice=int(input("Enter 1 for next medicine or enter 0 to exit: "))
print("-" * 95)    
print(f"{'Code':<20} {'Name':<20} {'Quantity':<20} {'Price':<20} {'Total':<20}")
print("-" * 95)
for i in range(len(sold_code)):
    print(f"{sold_code[i]:<20} {sold_name[i]:<20} {sold_qty[i]:<20} {sold_price[i]:<20} {sold_total[i]:<20}")
print("-" * 95)    
print("Total amount is: ",total)


