def count_vowels():
    s = input("Enter a string: ")
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count

print("Vowel count:", count_vowels())
