


students = []


def add_student():
    name = input("Talabaning ismi: ")
    age = int(input("Yoshi: "))
    grade = float(input("Bahosi: "))

    student = {
        "name": name,
        "age": age,
        "grade": grade
    }

    students.append(student)

    print(f"\n✅ {name} ro'yxatga qo'shildi!")


def show_students():
    if not students:
        print("\n❌ Hozircha talabalar yo'q.")
        return

    print("\n" + "=" * 50)
    print("            TALABALAR")
    print("=" * 50)

    for index, student in enumerate(students, start=1):
        print(
            f"{index}. "
            f"{student['name']} | "
            f"Yosh: {student['age']} | "
            f"Baho: {student['grade']}"
        )


def search_student():
    name = input("Qidirilayotgan ism: ").lower()

    found = False

    for student in students:
        if name in student["name"].lower():
            print("\n✅ Talaba topildi!")
            print(f"Ism: {student['name']}")
            print(f"Yosh: {student['age']}")
            print(f"Baho: {student['grade']}")

            found = True

    if not found:
        print("\n❌ Bunday talaba topilmadi.")


def delete_student():
    show_students()

    if not students:
        return

    try:
        number = int(input("\nO'chirmoqchi bo'lgan talaba raqami: "))

        if number < 1 or number > len(students):
            print("❌ Noto'g'ri raqam.")
            return

        deleted = students.pop(number - 1)

        print(f"✅ {deleted['name']} o'chirildi.")

    except ValueError:
        print("❌ Raqam kiriting!")


def statistics():
    if not students:
        print("\n❌ Statistikani chiqarish uchun talabalar kerak.")
        return

    total = len(students)

    average = sum(
        student["grade"]
        for student in students
    ) / total

    best_student = max(
        students,
        key=lambda student: student["grade"]
    )

    worst_student = min(
        students,
        key=lambda student: student["grade"]
    )

    print("\n" + "=" * 50)
    print("              STATISTIKA")
    print("=" * 50)

    print(f"👨‍🎓 Talabalar soni: {total}")
    print(f"📊 O'rtacha baho: {average:.2f}")
    print(
        f"🏆 Eng yuqori baho: "
        f"{best_student['name']} "
        f"({best_student['grade']})"
    )
    print(
        f"📉 Eng past baho: "
        f"{worst_student['name']} "
        f"({worst_student['grade']})"
    )


while True:

    print("\n" + "=" * 50)
    print("       🎓 STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)

    print("1. Talaba qo'shish")
    print("2. Barcha talabalarni ko'rish")
    print("3. Talaba qidirish")
    print("4. Talabani o'chirish")
    print("5. Statistikani ko'rish")
    print("6. Dasturdan chiqish")

    choice = input("\nTanlang: ")

    if choice == "1":
        try:
            add_student()
        except ValueError:
            print("❌ Yosh va bahoni raqam bilan kiriting!")

    elif choice == "2":
        show_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        statistics()

    elif choice == "6":
        print("\n👋 Dastur tugadi.")
        break

    else:
        print("\n❌ Noto'g'ri tanlov!")
