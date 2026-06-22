bal = 50000
got = 0
while bal > 0:
     withdrawal=int(input("Enter withdrawal amount(if you exit press -1): "))
     if withdrawal == -1:
         break
     if bal >= withdrawal:
         bal = bal-withdrawal
         got += withdrawal
     else:
         print("Insufficient balance")
print("Remaining balance is: ",bal)
print("Total withdrawal is: ",got)

         
     
     
