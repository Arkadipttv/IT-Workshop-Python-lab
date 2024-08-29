def pangram(word: str):
    s = set()
    for i in word.lower():
        if 'a'<=i<='z':
            s.add(i)
    
    if len(s) == 26:
        print("Pangram")
    else:
        print("Not Pangram")
        
sentence = str(input("Enter a String: "))

pangram(sentence)
