# X PATTERN

def x_pattern(n):
    # UPPER HALF
    for i in range(n,0,-1):
        print(' ' * (n - i),end = '')
        print('*',end = '')
        if i > 1:
            print(' ' * (2 * i - 3),end = '')
            print('*',end = '')
        print()

    # LOWER HALF
    for j in range(2,(n+1)):
        print(' ' * (n - j),end = '')
        print('*',end = '')
        if j > 1:
            print(' ' * (2 * j - 3),end = '')
            print('*',end = '')
        print()
x_pattern(5)

