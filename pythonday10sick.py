#yo bro anyone reading this code , i am sick today 13-11-2026 , So just a simple code   100F fever so 
#today imma gonna make a farenheit to celsius converter and celsius to fahrenheit converter

temprature =float(input("Enter the temprature:"))
unit = input("Define the unit that you have entered (C or F):").upper().strip()

if unit == "C":
    result = (temprature * 1.8) + 32
    print (f"your temperature in farenheit is {round (result,3)}")

#sorry guys i was so tired i didnt write farenheit to celcius converter (apologies)
