basic_salary=float(input("Enter the basic salary: "))
working_days=int(input("Enter the number of working days: "))
extra_hours=int(input("Enter the number of extra hours: "))
perfomance_allowance=working_days*basic_salary*0.05
extra_hours_allowance=extra_hours*250
total_salary=basic_salary+perfomance_allowance+extra_hours_allowance
tax=total_salary*0.12
net_salary=total_salary-tax
print("The net salary is: ", net_salary)