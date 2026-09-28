
# labe2_purchase_quote.py

# Neden input() aritmetik işlemden önce dönüştürülmelidir?
# Açıklama: input() fonksiyonu kullanıcıdan gelen veriyi her zaman string (metin) 
# tipinde alır. Stringler üzerinde matematiksel toplama veya çarpma yapılamaz 
# (string çarpımı metni tekrarlar, toplama ise uç uca ekler). Bu yüzden sayısal 
# işlemler için int() veya float() dönüşümü zorunludur.

# 1. Ürün Bilgileri
item1_name = input("Enter first item name: ")
item1_qty = int(input(f"Enter quantity for {item1_name}: "))
item1_price = float(input(f"Enter unit price for {item1_name}: "))

# 2. Ürün Bilgileri
item2_name = input("\nEnter second item name: ")
item2_qty = int(input(f"Enter quantity for {item2_name}: "))
item2_price = float(input(f"Enter unit price for {item2_name}: "))

# Kargo ve Vergi Oranı
delivery_fee = float(input("\nEnter delivery fee: "))
tax_percentage = float(input("Enter tax percentage (e.g., 10 for 10%): "))

# Hesaplamalar
line1_total = item1_qty * item1_price
line2_total = item2_qty * item2_price
subtotal = line1_total + line2_total

tax_amount = subtotal * (tax_percentage / 100)
final_total = subtotal + tax_amount + delivery_fee

# Çıktı / Fatura Özeti
print("\n" + "=" * 30)
print("PURCHASE QUOTE")
print("=" * 30)
print(f"{item1_name} ({item1_qty} x {item1_price:.2f} TRY): {line1_total:.2f} TRY")
print(f"{item2_name} ({item2_qty} x {item2_price:.2f} TRY): {line2_total:.2f} TRY")
print("-" * 30)
print(f"Subtotal: {subtotal:.2f} TRY")
print(f"Tax ({tax_percentage:.1f}%): {tax_amount:.2f} TRY")
print(f"Delivery Fee: {delivery_fee:.2f} TRY")
print("-" * 30)
print(f"Final Total: {final_total:.2f} TRY")
print("=" * 30)
