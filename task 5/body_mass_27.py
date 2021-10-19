s = str(input("Please choose your CI (Inches&Pounds/Meters&kilograms) "))
h = float(input("Input height "))
w = float(input("Input weight "))
if(s == "Inches&Pounds"):    
    print((w/(h*h))*703)
else:
    print(w/(h*h))
