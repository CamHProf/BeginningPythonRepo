# Kilometers to Smoots Calculator (0.0017018 km in a smoot)
km = float(input("Enter the distance in kilometers you have to calculate smoots: "))
smoots = km * 587.613
print(str(km) + " km = " + str(smoots) + " Smoots")

# Centimeters to Mickeys (0.0127 cm in a mickey.)
cm = float(input("Enter the distance in centimeters you have to calculate mickeys: "))
mickey = cm * 78.7402
print(str(cm) + " cm = " +str(mickey) + " Mickeys")

# Followers to Wheatons (500,000 followers to a Wheaton)
followers = float(input("How many followers $do you have on X (The Everything App)? "))
wheatons = followers / 500000
print(str(followers) + " followers = " + str(wheatons) + " Wheatons")

# Celsius to Kelvin (Kelvin starts out at 273.15 and increases and decreases per each singular celsius.)
celsius = float(input("Enter the temperature in celcius that you have to calculate Kelvin: "))
Kelvin = celsius + 273.15
print(str(celsius) + " celsius = " + str(Kelvin)  + " Kelvin")

# Fahrenheit to Kelvin (Formula: ({Farenheit} - 32) * 5/9 + 273.15
fahrenheit = float(input("Enter the temperature in fahrenheit that you want in Kelvin: "))
Kelvin = ((1 * fahrenheit) - 32) * 5 / 9 + 273.15
print(str(fahrenheit) + " F = " + str(Kelvin) + " K")
