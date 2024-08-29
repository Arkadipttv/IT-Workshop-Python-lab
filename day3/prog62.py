def ceaser(text,shift):
    result = ""
    for ch in text:
        if ch.islower():
            result += chr((ord(ch) + shift - 97) %26 + 97)
        elif ch.isupper():
            result += chr((ord(ch) + shift - 65) %26 +65)
        elif ch.isnumeric():
            result+=chr((ord(ch) + shift - 49) % 10 + 49)

        else:
            result += ch
    return result

text = input("Enter text: ")
shift = int(input("Enter shift value:"))
new = ceaser(text,shift)
print("Shifted : ",new)