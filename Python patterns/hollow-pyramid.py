# HOLLOW PYRAMID PATTERN

def hollow_pyramid(n):
    for i in range(1,(n+1)):
        print(' ' * (n - i),end = '')
        print('*',end = '')
        if i == 5:
            print('*' * (2 * i - 2),end = '')
        if i > 1 and i < n:
            print(' ' * (2 * i - 3),end = '')
            print('*',end = '')    
        print()
hollow_pyramid(5)

print()

# HOLLOW INVERTED PYRAMID PATTERN

def hollow_inverted_pyramid(n):
    for i in range(n,0,-1):
        print(' ' * (n - i),end = '')
        print('*',end = '')
        if i == 5:
            print('*' * (2 * i - 2),end = '')
        if i > 1 and i < n:
            print(' ' * (2 * i - 3),end = '')
            print('*',end = '')    
        print()
hollow_inverted_pyramid(5)
