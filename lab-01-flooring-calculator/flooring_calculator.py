
# Purpose: What does the program do (in a few sentences)?
# The purpose of this program is to calculate the amount and cost of purchasing flooring.
# List specific resources used to complete the assignment

# Prompt user for input
length = float(input("Room Length: "))
width = float(input("Room width : "))
cost = float(input("Cost per Sq. Foot: "))

# Calculate total square feet
square_ft = length * width

# Output
print("Square Feet: ", square_ft)

# Calculate Flooring cost 
cost_flooring = square_ft * cost

# Output
print("Flooring: ", cost_flooring)

# Calculate tax(7% of flooring cost)
tax = cost_flooring * 0.07

# Output
print("Tax:", tax)

# Calculate total amount due 
total_amount = cost_flooring + tax

# Output
print("Total Amount: ", total_amount)

