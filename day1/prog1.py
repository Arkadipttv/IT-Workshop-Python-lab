def calculate(years: int):
    #Number of Days
    print("Number of Days: ", years*365)
    #Number of Hours
    print("Number of Hours: ", years*365*24)
    #Number of Minutes
    print("Number of Minutes: ", years*365*24*60)
    #Number of Seconds
    print("Number of Seconds: ", years*365*24*60*60)

def leapyear():
    #asking user to enter a year
    print("Enter a year: ")
    y = int(input())

    if (y%400 == 0 or (y%100!=0 and y%4==0)):
        print(f"{y} is a Leap Year")
    else:
        print(f"{y} is not a Leap Year")

# print(type(y))



def main():
    #taking number of years as input from user
    y = int(input("Enter the number of Years: "))
    calculate(y)
    leapyear()

if __name__ == "__main__":
    main()