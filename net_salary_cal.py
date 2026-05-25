basic_salary = float(input("Enter the basic salary: "))
overtime_hours = float(input("Enter the number of overtime hours: "))
overtime_rate = 100
bonus = 0.1 * basic_salary
tax_percentage = 0.2
overtime_pay = overtime_hours * overtime_rate
gross_salary = basic_salary + overtime_pay + bonus
tax = tax_percentage * gross_salary
net_salary = gross_salary - tax
print("gross_salary: ", gross_salary)
print("tax: ", tax)
print("net_salary: ", net_salary)