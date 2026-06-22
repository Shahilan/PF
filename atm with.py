bal = 50000
got = 0
no_of_withdrawal = 0
while bal > 0:
     withdrawal=int(input("Enter withdrawal amount(if you exit press -1): "))
     if withdrawal == -1:
         break
     if bal >= withdrawal:
         bal = bal-withdrawal
         no_of_withdrawal += 1
         got += withdrawal
     else:
         print("Insufficient balance")
print("Total withdrawal: ",no_of_withdrawal)
print("Remaining balance is: ",bal)
print("Total withdrawal is: ",got)

         
     
     
