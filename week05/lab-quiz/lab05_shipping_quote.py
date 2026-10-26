# Difference between print and return:
# 'return' sends the calculated value back so we can use it in other functions or calculations.
# 'print' only shows the text on the screen for the user, it cannot be used in math operations.

# 1. Subtotal
def calculate_subtotal(price, quantity):
    return price * quantity

# 2. Discount Rate (10% discount for orders 100 and above)
def get_discount_rate(subtotal):
    if subtotal >= 100:
        return 0.10
    else:
        return 0.0

# 3. Shipping Fee (Free shipping for 150 and above, otherwise 20)
def calculate_shipping_fee(subtotal):
    if subtotal >= 150:
        return 0
    else:
        return 20

# 4. Final Total
def calculate_final_total(subtotal, discount_rate, shipping_fee):
    discount = subtotal * discount_rate
    total = (subtotal - discount) + shipping_fee
    return total

# Acceptance Check 3: Three assert checks (including threshold boundary)
assert calculate_subtotal(20, 5) == 100
assert get_discount_rate(100) == 0.10   # Threshold boundary check
assert get_discount_rate(99) == 0.0     # Below boundary check
assert calculate_shipping_fee(150) == 0 # Shipping boundary check

# Order 1
subtotal1 = calculate_subtotal(50, 4)
discount1 = get_discount_rate(subtotal1)
shipping1 = calculate_shipping_fee(subtotal1)
total1 = calculate_final_total(subtotal1, discount1, shipping1)

print("--- Order 1 ---")
print("Subtotal:", subtotal1)
print("Discount Rate:", discount1)
print("Shipping Fee:", shipping1)
print("Final Total:", total1)

# Order 2
subtotal2 = calculate_subtotal(15, 2)
discount2 = get_discount_rate(subtotal2)
shipping2 = calculate_shipping_fee(subtotal2)
total2 = calculate_final_total(subtotal2, discount2, shipping2)

print("\n--- Order 2 ---")
print("Subtotal:", subtotal2)
print("Discount Rate:", discount2)
print("Shipping Fee:", shipping2)
print("Final Total:", total2)