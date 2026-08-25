import random

secret = random.randint(1, 100)
attempts = 0

print("🎯 1 dan 100 gacha son o'yladim!")

while True:
    try:
        guess = int(input("Sonni toping: "))
        attempts += 1

        if guess < secret:
            print("📈 Kattaroq son kiriting!")
        elif guess > secret:
            print("📉 Kichikroq son kiriting!")
        else:
            print(f"🎉 To'g'ri! Siz {attempts} urinishda topdingiz!")
            break

    except ValueError:
        print("❌ Faqat raqam kiriting!")
