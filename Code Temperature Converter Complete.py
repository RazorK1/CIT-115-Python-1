#  Kyle Harris
#  CIT-115/115L Python
#  Code Temperature Converter 


#  Welcome Message
print("Not Prof. C’s Temp Converter:\n")
#  Spacer
print()


#  Prompt the user to enter a temperature and store it as a float
nTemperature = float(input("Enter a temperature: "))
#  Spacer
print()


#  Prompt the user for the temperature scale
sTempScale = input("Is the temp F for Fahrenheit or C for Celsius? ").strip().upper()
#  Spacer
print()

#  Check if the scale is either 'F' or 'C'
if sTempScale not in ('F', 'C'):
    print("You must enter a F or C")
    #  Spacer
    print()
    
else:
    #  Fahrenheit to Celsius conversion
    if sTempScale == 'F':
        
        #   Maximum temperature check
        if nTemperature > 212:
            print("Temp can not be > 212")
            #  Spacer
            print()
            
        else:
            nCelsius = (5.0 / 9) * (nTemperature - 32)
            print(f"The Celsius equivalent is: {nCelsius:.1f}")
            #  Spacer
            print()

    #  Celsius to Fahrenheit conversion
    elif sTempScale == 'C':
        
        #   Maximum temperature check
        if nTemperature > 100:
            print("Temp cannot be > 100")
            #  Spacer
            print()
            
        else:
            nFahrenheit = (9.0 / 5.0) * nTemperature + 32
            print(f"The Fahrenheit equivalent is: {nFahrenheit:.1f}")
            #  Spacer
            print()


#  Prevents the program from closing.
input("Press Enter to exit...")