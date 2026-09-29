import datetime
import math
import random


class AIAssistant:
    def __init__(self, name="PyAI"):
        self.name = name
        self.memory = []

    def remember(self, text):
        self.memory.append(text)

    def get_time(self):
        now = datetime.datetime.now()
        return now.strftime("%H:%M:%S")

    def get_date(self):
        now = datetime.datetime.now()
        return now.strftime("%d-%m-%Y")

    def calculate(self, expression):
        try:
            allowed = {
                "sqrt": math.sqrt,
                "pow": pow,
                "abs": abs,
                "round": round
            }

            result = eval(expression, {"__builtins__": {}}, allowed)
            return f"Natija: {result}"

        except Exception:
            return "❌ Hisoblashda xatolik yuz berdi."

    def random_answer(self):
        answers = [
            "Qiziq savol!",
            "Men buni o‘ylab ko‘rishim kerak 😄",
            "Hozircha bunga aniq javobim yo‘q.",
            "Bu haqida ko‘proq ma'lumot ber.",
            "Tushunarli 👍"
        ]

        return random.choice(answers)

    def process(self, message):
        text = message.lower().strip()

        # Salomlashish
        if text in ["salom", "hello", "hi"]:
            return f"Salom! Men {self.name}man 🤖"

        # Vaqt
        elif "vaqt" in text or "soat" in text:
            return f"Hozirgi vaqt: {self.get_time()}"

        # Sana
        elif "sana" in text or "bugun" in text:
            return f"Bugungi sana: {self.get_date()}"

        # Xotira
        elif text.startswith("eslab qol "):
            information = message[10:]
            self.remember(information)
            return f"✅ Eslab qoldim: {information}"

        # Xotirani ko‘rish
        elif text == "xotiram":
            if not self.memory:
                return "Xotiram hozircha bo‘sh."

            result = "🧠 Men eslab qolgan narsalar:\n"

            for i, item in enumerate(self.memory, start=1):
                result += f"{i}. {item}\n"

            return result

        # Kalkulyator
        elif text.startswith("hisobla "):
            expression = message[8:]
            return self.calculate(expression)

        # Tasodifiy son
        elif text == "random":
            number = random.randint(1, 100)
            return f"🎲 Tasodifiy son: {number}"

        # Chiqish
        elif text in ["exit", "quit", "xayr"]:
            return None

        # Oddiy javob
        else:
            return self.random_answer()


def main():
    ai = AIAssistant("SardorAI")

    print("=" * 50)
    print("🤖 SardorAI ishga tushdi!")
    print("=" * 50)

    print("""
Buyruqlar:

salom
vaqt
bugun
eslab qol ...
xotiram
hisobla 25 * 4
random
xayr
""")

    while True:
        user = input("\nSiz: ")

        response = ai.process(user)

        if response is None:
            print("AI: Xayr! 👋")
            break

        print("AI:", response)


if __name__ == "__main__":
    main()
