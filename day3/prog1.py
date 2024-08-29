def reduce_word(wrd):
    s=''
    for i in wrd:
        if s=='':
            s=s+i
        elif i==s[-1]:
            s=s[:-1]
        else:
            s=s+i
    return s

word = input("Enter a String in lowercase:")
word = word.lower()
if reduce_word(word) == '':
    print("Empty String")
else:
    print("Reduced String:")
    print(reduce_word(word))
