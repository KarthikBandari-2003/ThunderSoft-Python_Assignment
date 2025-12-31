numbers = [10, 15, 20, 23]
i = 0

while i < len(numbers):
    if numbers[i] % 2 == 0:
        print(numbers[i], "is Even")
    else:
        print(numbers[i], "is Odd")
    i += 1
