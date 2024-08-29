x = []
n = int(input("Enter number of elements: "))
print("Enter the values of x: ")
for i in range (n):
    x.append(int(input()))

sum = 0
for i in range(n):
    sum = sum + x[i]

mean = sum/n

variance = 0

for i in range(n):
    variance = (x[i] - mean) * (x[i] - mean)

variance = variance/n
standard_deviation = variance ** (0.5) 

print("Mean: ",mean)
print("Variance: ",variance)
print("Standard Deviation: ",standard_deviation)
