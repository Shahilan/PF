text=input("Enter a string: ")
count=0
i=0
while i < len(text):
    if text[i].lower() in "aeiou":
        count += 1
    i += 1
print("Number of vowels= " , count)    
