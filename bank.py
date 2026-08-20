balance = 1_000_000
pin_code = "1234"

print("=" * 40)
print("        🏦 PYTHON BANK")
print("=" * 40)

attempts = 3

while attempts > 0:
    pin = input("PIN kodni kiriting: ")

    if pin == pin_code:
        print("\n✅ Xush kelibsiz!")
        break
    else:
        attempts -= 1
        print(f"❌ PIN noto'g'ri. Qolgan urinish: {attempts}")

else:
    print("🚫 Kartangiz bloklandi!")
    exit()


while True:
    print("\n" + "=" * 40)
    print("1. 💰 Balansni ko'rish")
    print("2. 💵 Pul yechish")
    print("3. 💳 Pul qo'yish")
    print("4. 🔄 Pul o'tkazish")
    print("5. 🚪 Chiqish")
    print("=" * 40)

    choice = input("Tanlang: ")

    # BALANS
    if choice == "1":
        print(f"\n💰 Balansingiz: {balance:,} so'm")

    # PUL YECHISH
    elif choice == "2":
        try:
            amount = int(input("Yechmoqchi bo'lgan summa: "))

            if amount <= 0:
                print("❌ Summa 0 dan katta bo'lishi kerak.")

            elif amount > balance:
                print("❌ Hisobingizda yetarli pul yo'q.")

            else:
                balance -= amount
                print(f"✅ {amount:,} so'm yechildi.")
                print(f"💰 Qolgan balans: {balance:,} so'm")

        except ValueError:
            print("❌ Faqat raqam kiriting!")

    # PUL QO'YISH
    elif choice == "3":
        try:
            amount = int(input("Qo'ymoqchi bo'lgan summa: "))

            if amount <= 0:
                print("❌ Summa 0 dan katta bo'lishi kerak.")

            else:
                balance += amount
                print(f"✅ {amount:,} so'm hisobingizga qo'shildi.")
                print(f"💰 Yangi balans: {balance:,} so'm")

        except ValueError:
            print("❌ Faqat raqam kiriting!")

    # PUL O'TKAZISH
    elif choice == "4":
        receiver = input("Qabul qiluvchining ismi: ")

        try:
            amount = int(input("O'tkaziladigan summa: "))

            if amount <= 0:
                print("❌ Noto'g'ri summa.")

            elif amount > balance:
                print("❌ Hisobingizda yetarli pul yo'q.")

            else:
                balance -= amount

                print("\n✅ Pul muvaffaqiyatli o'tkazildi!")
                print(f"👤 Qabul qiluvchi: {receiver}")
                print(f"💸 Summa: {amount:,} so'm")
                print(f"💰 Qolgan balans: {balance:,} so'm")

        except ValueError:
            print("❌ Faqat raqam kiriting!")

    # CHIQISH
    elif choice == "5":
        print("\n👋 Tashrifingiz uchun rahmat!")
        print(f"💰 Yakuniy balans: {balance:,} so'm")
        break

    else:
        print("❌ Bunday menyu mavjud emas!")
