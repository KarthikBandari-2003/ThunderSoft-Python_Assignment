def palindrome(num):
    original = num
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10

    if original == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")

palindrome(121)
