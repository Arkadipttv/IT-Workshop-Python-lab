str_list = []

print("Enter the number of words: ")
num = int(input())

if num == 0:    
    print("There are no words")

    exit()

print("Enter the words")
for i in range(0, len(str_list)):
    str_list.append(str(input()))
maximum = str_list[0]
for i in range(0, len(str_list)):
    if maximum<len(str_list[i]):
        maximum = len(str_list[i])

print("Length of Longest String: ", maximum)