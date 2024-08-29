num = []
den = []
fraction = []
print("Enter the number of terms:")
n = int(input())
print("Enter the Numerators")
for i in range (n): num.append(int(input()))
print("Enter the Denominators")
for i in range (n): den.append(int(input()))
print("Numerator: ", num)
print("Denominator: ", den)
for i in range (n): fraction.append(num[i]/den[i])
print("Fraction: ", fraction)

