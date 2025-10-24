def get_valid_mark(subject):
    """Get a valid mark between 0–100 for a subject."""
    while True:
        try:
            mark = int(input(f"Enter marks for {subject} (0–100): "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("❌ Marks must be between 0 and 100.")
        except ValueError:
            print("❌ Please enter a valid number.")


def get_grade(avg):
    """Return grade based on average marks."""
    if 95 <= avg <= 100:
        return "A"
    elif 90 <= avg <= 94:
        return "A-"
    elif 87 <= avg <= 89:
        return "B+"
    elif 85 <= avg <= 86:
        return "B"
    elif 80 <= avg <= 84:
        return "B-"
    elif 77 <= avg <= 79:
        return "C+"
    elif 70 <= avg <= 76:
        return "C"
    elif 60 <= avg <= 69:
        return "D"
    elif 40 <= avg <= 59:
        return "E"
    else:
        return "F"


students = []


def add_student():
    """Add a new student and their subject marks."""
    print("\n📝 Enter student details:")
    name = input("Name: ")
    lang = get_valid_mark("Language")
    eng = get_valid_mark("English")
    math = get_valid_mark("Math")
    sci = get_valid_mark("Science")
    social = get_valid_mark("Social")

    student = {
        "Name": name,
        "Lang": lang,
        "Eng": eng,
        "Math": math,
        "Sci": sci,
        "Social": social
    }
    students.append(student)
    print(f"✅ Student '{name}' added successfully.")


def show_averages_and_grades():
    """Display each student's marks, average, and grade."""
    if not students:
        print("⚠️ No student data available.")
        return

    print("\n📊 Students Average and Grade:")
    for student in students:
        print(f"\n👤 {student['Name']}")
        subjects = ["Lang", "Eng", "Math", "Sci", "Social"]
        marks = [student[subj] for subj in subjects]
        avg = sum(marks) / len(subjects)
        grade = get_grade(avg)

        # Print marks and check for fails
        failed_subjects = []
        for subj in subjects:
            mark = student[subj]
            print(f"  {subj}: {mark}")
            if mark < 40:
                failed_subjects.append(subj)

        # Show results
        print(f"  Average Marks: {round(avg, 2)}")
        print(f"  Grade: {grade}")

        if failed_subjects:
            print(f"  ⚠️ FAIL in: {', '.join(failed_subjects)}")
            print("  Overall Result: ❌ FAIL")
        else:
            print("  Overall Result: ✅ PASS")


def show_highest_marks():
    """Show each student's highest mark."""
    if not students:
        print("⚠️ No student data available.")
        return

    print("\n🏆 Highest Marks per Student:")
    for student in students:
        subjects = ["Lang", "Eng", "Math", "Sci", "Social"]
        highest = max(student[subj] for subj in subjects)
        print(f"{student['Name']}: Highest Mark = {highest}")


def show_math_top_scorers():
    """Show students with Math >= 85."""
    if not students:
        print("⚠️ No student data available.")
        return

    print("\n📈 Students with Math ≥85:")
    found = False
    for student in students:
        if student["Math"] >= 85:
            print(f"- {student['Name']} ({student['Math']})")
            found = True
    if not found:
        print("No student scored 85 or above in Math.")


# ===============================
# 📋 Main menu loop
# ===============================
while True:
    print("\n📋 MENU")
    print("1. Add student")
    print("2. Show average and grade")
    print("3. Show highest mark of each student")
    print("4. Show students who scored ≥85 in Math")
    print("5. Exit")

    choice = input("Enter your choice (1–5): ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        show_averages_and_grades()
    elif choice == "3":
        show_highest_marks()
    elif choice == "4":
        show_math_top_scorers()
    elif choice == "5":
        print("👋 Exiting program. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please enter a number from 1 to 5.")
