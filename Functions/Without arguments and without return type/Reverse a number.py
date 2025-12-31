def reverse_number():
    num = int(input("Enter a number: "))
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    print("Reversed number:", rev)

reverse_number()
