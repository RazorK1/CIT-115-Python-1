#  Kyle Harris
#  CIT-115/115L Python
#  Compound Interest 


#  Constants for user prompts
INPUT_PRINCIPAL = "Enter the starting principal: "
INPUT_RATE = "Enter the annual interest rate: "
INPUT_COMPOUNDING = "How many times per year is the interest compounded?: "
INPUT_PERIODS = "For how many years will the account earn interest?: "


#  Get user input
#  Principal Investment
nPrincipal = float(input(INPUT_PRINCIPAL))  
#  Spacer
print()

#  Convert percentage to decimal
nRate = float(input(INPUT_RATE)) / 100  
#  Spacer
print()

#  Compounding frequency
nCompounding = int(input(INPUT_COMPOUNDING))  
#  Spacer
print()

#  Number of years
nPeriods = float(input(INPUT_PERIODS))  
#  Spacer
print()


#  Calculate Future Value using the compound interest formula
nFutureValue = nPrincipal * (1 + nRate / nCompounding) ** (nCompounding * nPeriods)


#  Format and display the output
print(f"At the end of {nPeriods} years you will have: ${nFutureValue:.2f}")
#  Spacer
print()


#  Prevents the program from closing.
input("Press Enter to exit...")