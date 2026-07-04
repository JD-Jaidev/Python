# RIGHT TRIANGLE PATTERN

def triangle_pattern(n):
    for i in range(1,n + 1):
        print(i * '*')
triangle_pattern(5)
print()

# RIGHT TRIANGLE PATTERN INVERTED

def triangle_pattern_inverted(n):
    for i in range(n,0,-1):
        print(i * '*')
triangle_pattern_inverted(5)
print()

# RIGHT TRIANGLE PATTERN USING NUMBERS - 1

def triangle_number_pattern1(n):
    for i in range(1,6):
        print(str(i) * i)
triangle_number_pattern1(5)
print()

# RIGHT TRIANGLE PATTERN USING NUMBERS - 2

def triangle_number_pattern2(n):
    for i in range(1,6):
        for j in range(1,i + 1):  
            print(j,end = '')
        print()
triangle_number_pattern2(5)
print()

# RIGHT MIRROR TRIANGLE PATTERN

def triangle_mirror_pattern(n):
    for i in range(1,n+1):
        print(' ' * (n - i) + '*' * i)
triangle_mirror_pattern(5)
print()

# RIGHT MIRROR TRIANGLE PATTERN INVERTED

def triangle_mirror_pattern_inverted(n):
    for i in range(n,0,-1):
        print(' ' * (n - i) + '*' * i)
triangle_mirror_pattern_inverted(5)
print()
