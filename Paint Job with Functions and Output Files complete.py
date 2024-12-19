#  Kyle Harris
#  CIT-115/115L Python
#  Paint Job with Functions and Output Files

#  Import necessary module
import math

#  1.  Function for getting validated float input
def getFloatInput(prompt):
    while True:
        try:
            fValue = float(input(prompt))
            if fValue > 0:  # Ensuring non-zero and positive
                return fValue
            else:
                print("Error: Value must be greater than zero. Please try again.")
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

#  2.  Prompt for state and customer last name
def getState():
    return input("Enter the state abbreviation (e.g., CT, MA, ME): ").strip().upper()

def getCustomerLastName():
    return input("Customer's Last Name: ").strip()

#  3.  Calculation functions
def getGallonsOfPaint(square_feet, feet_per_gallon):
    return math.ceil(square_feet / feet_per_gallon)

def getLaborHours(gallons, hours_per_gallon):
    return gallons * hours_per_gallon

def getLaborCost(labor_hours, charge_per_hour):
    return labor_hours * charge_per_hour

def getPaintCost(gallons, paint_price):
    return gallons * paint_price

def getSalesTax(state):
    tax_rates = {
        "CT": 0.06,
        "MA": 0.0625,
        "ME": 0.085,
        "NH": 0.0,
        "RI": 0.07,
        "VT": 0.06,
    }
    return tax_rates.get(state, 0.0)

def showCostEstimate(
    square_feet, gallons, labor_hours, paint_cost, labor_cost, tax, total_cost
):
    #  Format and display the cost estimate
    print("\n=== Paint Job Estimate ===")
    print(f"Square Feet of Wall: {square_feet:.2f}")
    print(f"Gallons of Paint Required: {gallons}")
    print(f"Total Labor Hours: {labor_hours:.2f}")
    print(f"Paint Cost: ${paint_cost:.2f}")
    print(f"Labor Cost: ${labor_cost:.2f}")
    print(f"Sales Tax: ${tax:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")
    print("==========================")

#  4. Main function
def main():
    #  Prompt inputs
    fSquareFeet = getFloatInput("Enter wall space in square feet: ")
    fPaintPrice = getFloatInput("Enter paint price per gallon: ")
    fFeetPerGallon = getFloatInput("Enter feet per gallon: ")
    fLaborHoursPerGallon = getFloatInput("How many labor hours per gallon: ")
    fLaborChargePerHour = getFloatInput("Labor charge per hour: ")
    sState = getState()
    sCustomerLastName = getCustomerLastName()

    #  Calculations
    iGallons = getGallonsOfPaint(fSquareFeet, fFeetPerGallon)
    fLaborHours = getLaborHours(iGallons, fLaborHoursPerGallon)
    fLaborCost = getLaborCost(fLaborHours, fLaborChargePerHour)
    fPaintCost = getPaintCost(iGallons, fPaintPrice)
    fTaxRate = getSalesTax(sState)
    fSalesTax = (fLaborCost + fPaintCost) * fTaxRate
    fTotalCost = fLaborCost + fPaintCost + fSalesTax

    #  Display and save cost estimate
    showCostEstimate(fSquareFeet, iGallons, fLaborHours, fPaintCost, fLaborCost, fSalesTax, fTotalCost)

    #  Create output file
    output_file_name = f"{sCustomerLastName}_PaintJobOutput.txt"
    with open(output_file_name, "w") as file:
        file.write("=== Paint Job Estimate ===\n")
        file.write(f"Square Feet of Wall: {fSquareFeet:.2f}\n")
        file.write(f"Gallons of Paint Required: {iGallons}\n")
        file.write(f"Total Labor Hours: {fLaborHours:.2f}\n")
        file.write(f"Paint Cost: ${fPaintCost:.2f}\n")
        file.write(f"Labor Cost: ${fLaborCost:.2f}\n")
        file.write(f"Sales Tax: ${fSalesTax:.2f}\n")
        file.write(f"Total Cost: ${fTotalCost:.2f}\n")
        file.write("==========================\n")
    
    print(f"\nFile created: {output_file_name}")

#  5. Run the program
if __name__ == "__main__":
    main()

#  Prevents the program from closing.
input("Press Enter to exit...")