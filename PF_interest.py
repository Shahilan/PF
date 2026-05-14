principal_amount= float(input("Enter the principal amount: "))
annual_interest_rate= float(input("Enter the annual interest rate (in %): "))
number_of_years= int(input("Enter the number of years: "))
total_amount= principal_amount * (1 + annual_interest_rate / 100) ** number_of_years
total_interest= total_amount - principal_amount
print("total amount is: ",total_amount)
print("compound interest is: ",total_interest)
