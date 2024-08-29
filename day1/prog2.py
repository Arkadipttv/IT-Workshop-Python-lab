def calculate_amount(p: float, r:float, t:float):
    #Calculating Simple Interest
    si = (p*r*t)/100
    #Calculating Compound Interest
    ci = p*((1+(r/100))**t - 1)
    print("Amount after Simple Interest: ", (p + si))
    print("Amount after Compound Interest: ", (p + ci))
def main():
    p = float(input("Enter the Principal: "))
    r = float(input("Enter the Rate of Interest per annum: "))
    t = float(input("Enter the number of Years: "))
    calculate_amount(p,r,t)
if __name__ == "__main__":
    main()

