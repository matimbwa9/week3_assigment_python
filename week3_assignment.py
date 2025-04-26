def calculate_discount(price, discount_percent):
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        # If discount is less than 20%, return original price
        return price

# Prompt the user to enter the price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate and print the final price after applying the discount
final_price = calculate_discount(price, discount_percent)

print(f"The final price after applying the discount is: {final_price}")
