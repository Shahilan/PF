marks=int(input("Enter the marks: " ))
if marks < 0 or marks > 100:
    print("Invalid marks. Please enter marks between 0 and 100.")
else:
    if marks >= 50:
        print("pass")
    else:
        print("fail")