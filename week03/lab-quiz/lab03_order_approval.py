# Girdileri alma
order_amount = float(input("Enter order amount (TRY): "))
available_stock = int(input("Enter available stock: "))
requested_quantity = int(input("Enter requested quantity: "))
is_member_input = input("Is the customer a member? (yes/no): ").strip().lower()

is_member = (is_member_input == "yes") #True, False değeri alıyoruz

# Kontrol ve Onay Politikası
if requested_quantity <= 0:
    print("Order Rejected: Requested quantity must be greater than zero.")
elif requested_quantity > available_stock:
    print("Order Rejected: Insufficient stock available.")
else:
    # Sipariş onaylandı, indirim kontrolü
    discount = 0.0
    reason = "Standard order approved."

    # Mantıksal operatör (and) ve kural: üye VE tutar >= 500 TRY
    if is_member and order_amount >= 500:
        discount = order_amount * 0.10
        reason = "Member discount of 10% applied (order >= 500 TRY)."
    elif is_member and order_amount < 500:
        reason = "Member detected, but order is below 500 TRY threshold for discount."

    final_price = order_amount - discount

    print("--- Order Summary ---")
    print("Status: Approved")
    print(f"Reason: {reason}")
    print(f"Original Amount: {order_amount:.2f} TRY")
    print(f"Discount: {discount:.2f} TRY")
    print(f"Final Price: {final_price:.2f} TRY")