# 1. Girdilerin Kontrol Edilerek Alınması (Input Validation)

# Başlangıç bakiyesi negatif olamaz (>= 0)
while True:
    balance = float(input("Enter starting balance: "))
    if balance >= 0:
        break
    print("Starting balance cannot be negative. Try again.")

# Aylık birikim pozitif olmalı (> 0)
while True:
    deposit = float(input("Enter monthly deposit: "))
    if deposit > 0:
        break
    print("Monthly deposit must be positive. Try again.")

# Aylık faiz oranı negatif olamaz (>= 0)
while True:
    rate = float(input("Enter monthly interest rate (%): "))
    if rate >= 0:
        break
    print("Interest rate cannot be negative. Try again.")

# Hedef tutar pozitif olmalı (> 0)
while True:
    goal = float(input("Enter savings goal: "))
    if goal > 0:
        break
    print("Savings goal must be positive. Try again.")


# 2. Özel Durum Kontrolü: Başlangıç bakiyesi zaten hedefi karşılıyor mu?
if balance >= goal:
    print("\nStarting balance already meets or exceeds the savings goal.")
    print(f"Goal reached in 0 months. Final Balance: {balance:.2f}, Total Interest: 0.00")
else:
    # 3. Simülasyon Değişkenleri
    total_interest = 0.0
    months_passed = 0
    goal_reached = False

    # Tablo Başlığı
    print("\nMonth | Interest Earned | New Balance")
    print("-" * 37)

    # 4. Aylık Hesaplama (Maksimum 60 ay)
    for month in range(1, 61):
        months_passed = month

        # Adım A: Mevcut bakiyeye göre faiz hesapla
        interest_earned = balance * rate / 100
        total_interest += interest_earned

        # Adım B: Faizi ve aylık birikimi bakiyeye ekle
        balance += interest_earned + deposit

        # Adım C: Aylık tablo satırını yazdır
        print(f"{month:^5} | {interest_earned:^15.2f} | {balance:^11.2f}")

        # Adım D: Hedefe ulaşıldıysa döngüyü erken bitir (break şartı)
        if balance >= goal:
            goal_reached = True
            break

    # 5. Özet Sonuçlar
    print("\n--- Summary ---")
    if goal_reached:
        print(f"Goal reached in {months_passed} months!")
    else:
        print("Goal was not reached within 60 months.")

    print(f"Final Balance: {balance:.2f}")
    print(f"Total Interest Earned: {total_interest:.2f}")