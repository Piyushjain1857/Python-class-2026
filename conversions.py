# celsius to Fehrenheit
def Temprature_converter():
    celsius = float(input("Enter the Temp. in Celsius:-"))
    Fehrenheit = (celsius * 1.8) + 32
    print("The Temp. in Fehrenheit is:-", Fehrenheit)


# Km to Miles
def Distance_converter():
    Km = float(input("Enter the distance in KM:-"))
    miles = Km * 0.621371
    print("Distance In Miles:-", miles)


# Kg to Pound
def Weight_converter():
    Kg = float(input("Enter the weight in Kg:-"))
    Pound = Kg * 2.20462
    print("Weight in Pounds:-", Pound)


while True:
    print("-----Converters-----")
    print("1. Temprature_converter")
    print("2. Distance_converter") 
    print("3. Weight_converter")
    print("4. Exit")
    choice = int(input("Enter your choice "))

    if choice == 1:
        Temprature_converter()
    elif choice == 2:
        Distance_converter()
    elif choice == 3:
        Weight_converter()
    else:
        print("Exited")
        break
