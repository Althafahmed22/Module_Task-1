def reverse_string(s):
    return s[::-1]
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    if s == s[::-1]:
        return "Yes"
    else:
        print("No")
def capitalize_words(s):
    str = s.split(" ")
    result = [i.capitalize() for i in str]
    return result

