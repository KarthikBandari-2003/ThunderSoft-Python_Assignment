def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    print("Reversed number:", rev)

reverse_number(1234)
