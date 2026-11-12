#weight converter

weight = float(input("Enter your weight: "))
unit = input("Enter the unit that you entered as weight (KG or LBS):").upper().strip()

if unit == "KG":
    result = weight*2.205
    print(f"your weight in LBS is {round(result,3)} LBS")
elif unit == "LBS":
    result = weight/2.205
    print(f"your weight in KG is {round(result, 3)} KG")

else:
    print("invalid input .please use numbers")



