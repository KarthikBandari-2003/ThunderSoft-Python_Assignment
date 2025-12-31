def check_even_odd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd())
