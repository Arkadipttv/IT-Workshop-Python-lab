lst = []
n = int(input("Enter number of elements:"))
print("Enter the elements of list: ")
for i in range (n):
    lst.append(int(input()))
print("Original List: ", lst)
for i in range (n//2):
    temp = lst[i]
    lst[i] = lst[n-i-1]
    lst[n-i-1] = temp
print("Reversed List: ",lst)
