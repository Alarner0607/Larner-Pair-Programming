#Function for value conversion

def conversion():
    feet = int(input("Feet: "))  #Feet measurement input
    inches = int(input("Inches: "))   #Inches measurement input
    meters = (0.3048 * feet) + (0.0254 * inches)   #Conversion math
    print(f"{meters} Meters")   #Statement

#Enter values as only numbers 
#Run the function as just conversion()

conversion()

#Partner Notes: The code generally works as intended in normal cases however the converstion 
# of inputed values to integers may cause minor errors if the inputed number was not an integer 
# to begin with. The code does properly handle negative integers and the number 0.