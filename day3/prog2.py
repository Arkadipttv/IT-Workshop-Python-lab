def calculate(word:str):
    low = upp = 0
    for i in word:
        if i.islower():
            low = low + 1
        elif i.isupper():
            upp = upp + 1
    
    print(f"Lowercase Characters: {low}")
    print(f"Uppercase Characters: {upp}")


print("Enter a Sentence:")

sent = str(input())
calculate(sent)

