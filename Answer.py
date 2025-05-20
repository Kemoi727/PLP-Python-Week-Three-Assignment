#Function to calculate Discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Using the function with user input
# Prompt user for inputs
original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percentage)

# Print result
if discount_percentage >= 20:
    print(f"Discount applied. Final price is: ${final_price:.2f}")
else:
    print(f"No discount applied. Original price is: ${original_price:.2f}")
