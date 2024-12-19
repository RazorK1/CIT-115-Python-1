#  Kyle Harris
#  CIT-115/115L Python
#  Lists and Real Estate Analyzer


#  Prompts the user for a float input, validates it for positive numbers, non-zero, and invalid inputs.

def getFloatInput(prompt):
    

    
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be positive and greater than zero.")
                continue
            return value
        except ValueError:
            print("Input a number that is greater than 0.")


#  Calculates and returns the median of a list of numbers.
def getMedian(lstSalesList):
    
    n = len(lstSalesList)
    lstSalesList.sort()
    if n % 2 == 1:  #  Odd number of elements
        return lstSalesList[n // 2]
    else:  #  Even number of elements
        mid1 = n // 2
        mid2 = mid1 - 1
        return (lstSalesList[mid1] + lstSalesList[mid2]) / 2

def main():
    
    #  Main function to handle user input, process sales data, and display analytics.
    
    lstSalesList = []
    
    while True:
        #  Get user input for sales value
        fSalesPrice = getFloatInput("Enter property sales value: ")
        lstSalesList.append(fSalesPrice)
        
        #  Prompt user for another input
        while True:
            continue_input = input("Enter another value Y or N: ").strip().lower()
            if continue_input in {'y', 'n'}:
                break
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
        
        if continue_input == 'n':
            break

    #  Sort the list
    lstSalesList.sort()

    #  Display sorted sales list formatted as currency
    print("\nSales Data:")
    for sale in lstSalesList:
        print(f"${sale:,.2f}")

    #  Calculate and display analytics
    min_value = min(lstSalesList)
    max_value = max(lstSalesList)
    total = sum(lstSalesList)
    average = total / len(lstSalesList)
    median = getMedian(lstSalesList)
    commission = total * 0.03

    #  Display analytics
    print("\n")
    print(f"Minimum:      ${min_value:,.2f}")
    print(f"Maximum:      ${max_value:,.2f}")
    print(f"Total:        ${total:,.2f}")
    print(f"Average:      ${average:,.2f}")
    print(f"Median:       ${median:,.2f}")
    print(f"Commission:   ${commission:,.2f}")

#  Run the main function
if __name__ == "__main__":
    main()
    
#  Prevents the program from closing.
input("\nPress Enter to exit...")