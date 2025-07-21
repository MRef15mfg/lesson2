def is_palindrome(number):
    s = str(number)
    return s == s[::-1]

print(is_palindrome(9))