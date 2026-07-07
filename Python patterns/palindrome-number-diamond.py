# PALINDROME NUMBER DIAMOND PATTERN

def palindrome_number_diamond(n):
    # UPPER PART
    for i in range(1, n + 1):
        palindrome = int("1" * i) ** 2
        print(' ' * (n - i) + str(palindrome))

    # LOWER PART
    for i in range(n - 1,0,-1):
        palindrome = int("1" * i) ** 2
        print(' ' * (n - i) + str(palindrome))

palindrome_number_diamond(5)
