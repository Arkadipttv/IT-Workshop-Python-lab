def caesar_cipher(text: str, key: int):
    encoded_text = ""
    for ch in text:
        if ch.islower():
            encoded_text += chr((ord(ch) + key - 97) %26 + 97)
        elif ch.isupper():
            encoded_text += chr((ord(ch) + key - 65) %26 + 65)
        else:
            encoded_text += ch
    return encoded_text
    

text = input("Enter a String: ")
shift = int(input("Enter the OFFSET: "))
print("Encoded String: ")
encoded_word = caesar_cipher(text, shift)
print(encoded_word)