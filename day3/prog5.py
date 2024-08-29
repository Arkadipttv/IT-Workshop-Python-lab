word = str(input("Enter a word: "))

for i in word:
    if ord(i)-96 != word.count(i):
        print("Not Super ASCII")
        exit()

print("Super ASCII")