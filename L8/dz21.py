import string
def is_palindrome(text):
    text1 = text.lower().replace(" ", "")
    for sign_ in string.punctuation:
        if sign_ in text1:
            text1 = text1.replace(sign_, '')
    if text1 == text1[::-1]:
        return True
    else:
        return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
