#  Kyle Harris
#  CIT-115/115L Python
#  Compound Interest with Loops 


#  Compound Interest Program for Savings Goal

#  Import necessary module
import sys

#  Function to get validated positive numeric input
def get_positive_input(prompt, allow_zero=False):
    while True:
        try:
            value = float(input(prompt))
            # Check if the value is positive or zero (if allowed)
            if value > 0 or (allow_zero and value == 0):
                return value
            else:
                print("Input must be 0 or greater.")
        except ValueError:
            print("Input must be a positive numeric value.")

#  Get user inputs with validation
fDeposit = get_positive_input("What is the Original Deposit (positive value): ")
fInterestRate = get_positive_input("What is the Interest Rate (positive value): ") / 100
iMonths = int(get_positive_input("What is the Number of Months (positive value): "))
fGoal = get_positive_input("What is the Goal Amount (can enter 0 but not negative): ", allow_zero=True)

#  Calculate monthly interest rate
fMonthlyInterestRate = fInterestRate / 12

#  Step 4: Compound interest for the given number of months
print("\nMonthly Balance Calculation:\n")
for iMonth in range(1, iMonths + 1):
    fInterestForMonth = fDeposit * fMonthlyInterestRate
    fDeposit += fInterestForMonth
    # Output month number and account balance formatted as currency
    print(f"Month {iMonth}: ${fDeposit:,.2f}")

#  Step 5: Calculate months to reach savings goal
if fGoal > fDeposit:
    iGoalMonths = 0
    fAccountBalance = fDeposit
    
    #  Loop until account balance reaches or exceeds the goal
    while fAccountBalance < fGoal:
        fInterestForMonth = fAccountBalance * fMonthlyInterestRate
        fAccountBalance += fInterestForMonth
        iGoalMonths += 1

    iDisplayMonths = int(iGoalMonths + iMonth)
    print(f"\nIt will take:  {iDisplayMonths:,} months to reach your goal of ${fGoal:,.2f}.\n")
    
#  Prevents the program from closing.
input("Press Enter to exit...")
