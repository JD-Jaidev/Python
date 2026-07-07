# PALINDROME NUMBER PYRAMID PATTERN

def palindrome_number_pyramid(n):
    for i in range(1, n + 1):
        palindrome = int("1" * i) ** 2
        print(' ' * (n - i) + str(palindrome))
palindrome_number_pyramid(5)
