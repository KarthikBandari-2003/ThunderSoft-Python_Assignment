def is_palindrome(num):
    original = num
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return original == rev

print(is_palindrome(121))
