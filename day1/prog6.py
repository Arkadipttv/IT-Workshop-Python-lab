def grade_calculation(average: int):
    # Method of calculating grade
    if 91 <= average <= 100:
        return "O"
    elif 81 <= average <= 90:
        return "A+"
    elif 71 <= average <= 80:
        return "A"
    elif 61 <= average <= 70:
        return "B"
    elif 51 <= average <= 60:
        return "C"
    elif 41 <= average <= 50:
        return "D"
    elif 33 <= average <= 40:
        return "E"
    else:
        return "F"

def main():
    total = 0
    print("Enter marks in 5 subjects")
    for i in range(5):
        print(f"Subject {i + 1}:")
        sub = int(input())
        total = total + sub
    
    average = total/5
    print("Average Marks: ", int(average))

    print("Grade: ", grade_calculation(average))
    
if __name__ == "__main__":
    main()
