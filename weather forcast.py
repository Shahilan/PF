hum=int(input("Enter Humidity: "))
tem=int(input("Enter Temperature: "))
if hum>80:
        if tem>30:
             speed=int(input("Enter Wind Speed: "))
             if speed>40:
               print("Severe Strom Warning")
             else:
                  print("Heavy Rain Expected")
        else:
             print("Cloudy Weather")
else:
    if tem>35:
      print("Heat Wave Alert")
    else:
         print("Normal Weather")
         
