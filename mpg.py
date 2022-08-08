try:
    miles = float(input("Enter number of miles driven by vehicle: "))
    gallons = float(input("Enter number of gallons used: "))
    mpg = miles / gallons
    print("vehicle has efficiency of", mpg, "miles per gallon")
except:
    print("Invalid input received.")