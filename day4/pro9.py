def search_in_list(lst: list, srch:int):
    for i in lst:
        if srch in lst:
            return i
    
    return 0

lst = []
size = int(input("Enter size of list:"))
print("Enter the elements:")
for i in range (size):
    lst.append(int(input()))

print(lst)
search = int(input("Enter element to be searched:"))

if search_in_list(lst, search) != 0:
    print("Element found at index: ", search_in_list(lst, search))
    exit()

print("Element not found in list")
