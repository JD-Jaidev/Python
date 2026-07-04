# DIAMOND PATTERN

def diamond_pattern(n):
    # upper half
    for i in range(1,n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

    # lower half
    for j in range(n - 1,0,-1):
        print(' ' * (n - j) + '*' * (2 * j - 1))

diamond_pattern(5)
