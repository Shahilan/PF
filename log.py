log=int(input("if u registerd type 1 otherwise type 0: "))
if log == 1:
    sav=int(input("Enter your card value: "))
    if sav > 1000:
                pay=int(input("if your payment success type 1 otherwise type 0: "))
                if pay == 1:
                   print("payment succsessful")
                else:
                     print("payment not success")
    else:
        print("invalid credit")
else:
    print("not login")
