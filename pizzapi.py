#Write a Python program (pizzapi.py) that prompts for the diameter of a pizza,
#the total price of the pizza and the number of slices in the pizza.
#Calculate the area and the cost for a single slice of pizza.

#Declare constant to store fixed value
PI = 3.14

    
#Declare and initialize whole(integer)variable 
numSlices = 0
#Declare and initialize real (decimal) variables 
pizzaDiameter = pizzaCost = radius = areaOfPizza = areaOfSingleSlice = costOfSingleSlice = 0.0


#Display introduction to the user
print("\nWELCOME TO BROWARD COLLEGE PIZZERIA!\n\n")

#Prompt user for the diameter of a pizza
pizzaDiameter = float(input("Enter the diameter of the pizza(in): "))



#Prompt user for the total price of the pizza
pizzaCost = float(input("\nEnter the total cost of the pizza: "))


#Prompt user for the number of slices in the pizza
numSlices = int(input("\nEnter number of slices in the pizza: "))
#Diaplay empty lines
print("\n\n\n")
#Display stars
print("******************************************************")


#Calculations
#Find out radius to calculate the area of pizza (radius = diameter / 2)
radius = pizzaDiameter/2
#calculate the area of pizza (area = pi " radius * radus)
areaOfPizza = PI * radius * radius
#calculate the area of a single slice of pizza
areaOfSingleSlice = areaOfPizza / numSlices
#calculate the cost of a single slice of pizza
costOfSingleSlice = pizzaCost / numSlices

    
#Display the area of a single slice of pizza to user
print(f"\n\n\nArea of single slice of pizza: {areaOfSingleSlice:.2f} sq. in.")
#Display the cost of a single slice of pizza to user
print(f"\nCost of a single slice of pizza: ${costOfSingleSlice:.2f}")

#Display outro
print("\n\nThank you for buying pizza!!")



