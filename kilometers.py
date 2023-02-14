#Program to calculate the number of miles traveled
#based on user input of kilometers

#Define main():
def main():
    #Declare constant to store conversion of 0.6214
    CONVERSION = 0.6214

    #Declare and initialize real variables to store kilometers and miles
    kilometers = miles = 0.0
    #Declare string variable to store name
    name = ""
    
    #Display Introduction
    print("Welcome to my miles conversion program!\n")
    print("I will ask for a number of kilometers traveled and then")
    print("display the number of miles you traveled\n\n")

    #Prompt user for name
    name = input("What is your name? ")

    #prompt user for kilometers traveled
    kilometers = float(input("\nHow many kilometers did you travel? "))
    
    #Set miles = kilometers * conversion
    miles = kilometers * CONVERSION
    
    #Display name and miles to user
    #This way is old - do not use it
    print("\n%.2f" % kilometers, "kilometers equals", "%.2f" % miles, "miles!")

    #.format is newer, but still not the newest or prefered
    print("\nGreat job" , name, "you've traveled {:.2f}".format(miles), "miles!")
    
    #f formating is the best way to go
    print(f"\nGreat job {name}, {kilometers:.1f} kilometers equals {miles:.2f} miles!")
    
    #Display outro
    print("\nThank you for using my conversion program!")
    

#call or invoke main function
main()
