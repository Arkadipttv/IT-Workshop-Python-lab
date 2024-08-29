def grade_calculation(marks: float):
    # Method of calculating grade
    if 91 <= marks <= 100:
        return "O"
    elif 81 <= marks <= 90:
        return "A+"
    elif 71 <= marks <= 80:
        return "A"
    elif 61 <= marks <= 70:
        return "B"
    elif 51 <= marks <= 60:
        return "C"
    elif 41 <= marks <= 50:
        return "D"
    elif 33 <= marks <= 40:
        return "E"
    else:
        return "F"

def main():
    print("Enter marks in 5 subjects")

    subject = []
    for i in range(5):
        print(f"Subject {i + 1}:")
        sub = int(input())
        subject.append(sub)

    print("Gradation Table:")
    for i in range(5):
        grade = grade_calculation(subject[i])
        print(f"Subject {i + 1}: {grade}")

if __name__ == "__main__":
    main()
