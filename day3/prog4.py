word = str(input("Enter a Word: "))
word = word.lower()
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
