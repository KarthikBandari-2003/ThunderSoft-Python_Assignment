def palindrome():
    num = int(input("Enter a number: "))
    original = num
    rev = 0

    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10

    if original == rev:
        return "Palindrome"
    else:
        return "Not Palindrome"

print(palindrome())
