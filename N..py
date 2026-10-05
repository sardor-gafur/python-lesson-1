import random
from datetime import datetime

print("=" * 45)
print("🤖 PYTHON AI CHATBOT")
print("=" * 45)

name = input("Ismingiz: ")

responses = {
    "salom": [
        f"Salom, {name}! 👋",
        f"Assalomu alaykum, {name}!",
        f"Salom {name}, qanday yuribsiz?"
    ],
    "qalaysan": [
        "Yaxshi, rahmat! 😎",
        "Ajoyib! Siz-chi?",
        "Hammasi joyida!"
    ],
    "isming nima": [
        "Mening ismim PythonBot 🤖",
        "Meni PythonBot deb atashingiz mumkin."
    ],
    "nima qila olasan": [
        "Men suhbatlasha olaman, vaqtni ko‘rsataman va oddiy hisob-kitoblar qilaman.",
        "Men Python asosida yaratilgan oddiy chatbotman."
    ]
}


def calculate():
    try:
        a = float(input("Birinchi son: "))
        operator = input("Amal (+, -, *, /): ")
        b = float(input("Ikkinchi son: "))

        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            if b == 0:
                return "0 ga bo‘lish mumkin emas!"
            result = a / b
        else:
            return "Noto‘g‘ri amal!"

        return f"Natija: {result}"

    except ValueError:
        return "Iltimos, son kiriting!"


def chatbot():
    while True:
        message = input("\nSiz: ").lower().strip()

        if message == "exit":
            print("Bot: Ko‘rishguncha! 👋")
            break

        elif message == "vaqt":
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Bot: Hozirgi vaqt: {current_time}")

        elif message == "hisobla":
            print("Bot:", calculate())

        elif message in responses:
            print("Bot:", random.choice(responses[message]))

        else:
            print("Bot: Buni hali tushunmadim 🤔")
            print("Bot: 'salom', 'qalaysan', 'vaqt' yoki 'hisobla' deb yozib ko‘ring.")


chatbot()
