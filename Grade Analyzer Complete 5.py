#  Kyle Harris
#  CIT-115/115L Python
#  Code Grade Analyzer 


# Program to calculate the test average and determine letter grade with an option to drop the lowest score.

# Step 1: Prompt for the person's name
sName = input("Name of person that we are calculating the grades for: ")
#  Spacer
print()

# Step 2: Prompt for four test scores and ensure only whole numbers are accepted
try:
    iTest1 = int(input("Test 1: "))
    iTest2 = int(input("Test 2: "))
    iTest3 = int(input("Test 3: "))
    iTest4 = int(input("Test 4: "))
    #  Spacer
    print()
except ValueError:
    print("Invalid input. Only whole numbers are accepted.")
    #  Spacer
    print()
    #  Prevents the program from closing.
    input("Press Enter to exit...")
    exit()
    
# Step 3: Prompt for whether the lowest grade should be dropped
sDropLowest = input("Do you wish to Drop the Lowest Grade Y or N? ").upper()
#  Spacer
print()

# Step 4: Check that no test score is negative
if iTest1 < 0 or iTest2 < 0 or iTest3 < 0 or iTest4 < 0:
    print("Test scores must be greater than 0")
    #  Spacer
    print()
    #  Prevents the program from closing.
    input("Press Enter to exit...")
    exit()

# Step 5: Validate that Drop Lowest input is either 'Y' or 'N'
if sDropLowest not in ('Y', 'N'):
    print("Enter Y or N to Drop the Lowest Grade.")
    #  Spacer
    print()
    #  Prevents the program from closing.
    input("Press Enter to exit...")
    exit()

# Step 6: Calculate the average score with or without dropping the lowest grade
fAverage = 0.0  # Initialize the average variable

if sDropLowest == 'Y':
    # Determine the lowest score manually (without using min() or lists)
    if iTest1 <= iTest2 and iTest1 <= iTest3 and iTest1 <= iTest4:
        fAverage = (iTest2 + iTest3 + iTest4) / 3
    elif iTest2 <= iTest1 and iTest2 <= iTest3 and iTest2 <= iTest4:
        fAverage = (iTest1 + iTest3 + iTest4) / 3
    elif iTest3 <= iTest1 and iTest3 <= iTest2 and iTest3 <= iTest4:
        fAverage = (iTest1 + iTest2 + iTest4) / 3
    else:
        fAverage = (iTest1 + iTest2 + iTest3) / 3
else:
    # Calculate the average of all four test scores
    fAverage = (iTest1 + iTest2 + iTest3 + iTest4) / 4

# Step 7: Ensure the average is a float with one decimal
fAverage = round(fAverage, 1)

# Step 8: Determine the letter grade based on the calculated average
if fAverage >= 97.0:
    sGrade = "A+"
elif fAverage >= 94.0:
    sGrade = "A"
elif fAverage >= 90.0:
    sGrade = "A-"
elif fAverage >= 87.0:
    sGrade = "B+"
elif fAverage >= 84.0:
    sGrade = "B"
elif fAverage >= 80.0:
    sGrade = "B-"
elif fAverage >= 77.0:
    sGrade = "C+"
elif fAverage >= 74.0:
    sGrade = "C"
elif fAverage >= 70.0:
    sGrade = "C-"
elif fAverage >= 67.0:
    sGrade = "D+"
elif fAverage >= 64.0:
    sGrade = "D"
elif fAverage >= 60.0:
    sGrade = "D-"
else:
    sGrade = "F"

# Step 13 and 14: Output the name, calculated average, and letter grade
print(f"{sName} test average is: {fAverage:.1f}")
print(f"Letter Grade for the Test is: {sGrade}")
#  Spacer
print()


#  Prevents the program from closing.
input("Press Enter to exit...")
exit()