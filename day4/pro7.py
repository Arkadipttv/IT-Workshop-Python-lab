lst1 = []
lst2 = []

n = int(input("Enter the no. of elements:"))

print("Enter elements of List 1: ")
for i in range(n):
    lst1.append(int(input()))

print("Enter elements of List 2: ")
for i in range(n):
    lst2.append(int(input()))

for i in range(n):
    if lst1[i] != lst2[i]:
        print("They differ at index ", i)
        exit()

print("They are equal")