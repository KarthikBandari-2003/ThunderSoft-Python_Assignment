num = 121
temp = num
rev = 0

for _ in range(len(str(num))):
    rev = rev * 10 + temp % 10
    temp //= 10

if num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
