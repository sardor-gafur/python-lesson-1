import random

secret_number = random.randint(1, 100)
attempts = 0

print("🎮 Son topish o'yini!")
print("Men 1 dan 100 gacha bitta son o'yladim.")

while True:
    try:
        guess = int(input("Sonni toping: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("⚠️ 1 dan 100 gacha son kiriting.")
            continue

        if guess < secret_number:
            print("📈 Kattaroq son kiriting!")
        elif guess > secret_number:
            print("📉 Kichikroq son kiriting!")
        else:
            print(f"🎉 To'g'ri! Son {secret_number} edi.")
            print(f"Urinishlar soni: {attempts}")
            break

    except ValueError:
        print("❌ Faqat son kiriting!")
