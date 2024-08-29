L = []
M = []
N = []

size = int(input("Enter size of L and M: "))

print("Enter elements of L: ")

for i in range(size):
    L.append(int(input()))

print("Enter elements of M: ")

for i in range(size):
    M.append(int(input()))

for i in range(size):
    N.append(L[i]+M[i])




print("L: ", L)
print("M: ", M)
print("N: ", N)