def calculate(n:int):
    rev = 0
    copy = n
    #Calculating reverse of the number
    while(n!=0):
        rev = rev*10 + (n%10)
        n = n//10
    print(f"Reverse of {copy} is {rev}")

    #Checking if number is odd or even
    if(copy%2 == 0):
        print(f"{copy} is even")
    else:
        print(f"{copy} is odd")

def main():
    print("Enter a Number:")
    num = int(input())
    calculate(num)

if __name__ == "__main__":
    main()