vowels=['a','e','i','o','u']
def count_vowels(s):
    str=s.lower()
    c=0
    for i in str:
        if i in vowels:
            c+=1
    return c