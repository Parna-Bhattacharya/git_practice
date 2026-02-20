def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks > 40 and marks == 40:
        return "D"
    elif marks > 30 and marks == 30:
        return "G"
    else:
        return "Fail"


def main():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    grade = calculate_grade(marks)

    print(f"Student: {name}")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()