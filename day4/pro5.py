lst = []
n = int(input("Enter the no. of elements: "))
print("Enter the elements")
for i in range(n):
    lst.append(int(input()))
print(lst)
low = int(input("Enter lower index:"))
high = int(input("Enter upper index:"))
max = min = lst[0]
for i in range(low, high+1):
    if max<lst[i]:
        max = lst[i]
    if min>lst[i]:
        min = lst[i]

print("Maximum Element: ", max)
print("Minimum Element: ", min)


