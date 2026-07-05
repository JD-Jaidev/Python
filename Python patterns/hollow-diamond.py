# HOLLOW DIAMOND PATTERN

n = 5
def hollow_diamond_pattern(n):
    # UPPER HALF
    for i in range(1,(n + 1)):
        print(" " * (n - i),end = '')
        print("*",end = '')

        if i > 1:
            print(" " * (2 * i - 3),end = '')
            print("*",end = '')

        print()

    #LOWER HALF
    for j in range((n - 1),0,-1):
        print(" " * (n - j), end="")
        print("*", end="")

        if j > 1:
            print(" " * (2 * j - 3), end="")
            print("*", end="")

        print()

hollow_diamond_pattern(5)
