# REPEATED NUMBER PYRAMID

def repeated_number_pyramid(n):
    for i in range(1,(n + 1)):
        print(' ' *(n - i) + str(i) * (2 * i - 1))
repeated_number_pyramid(5)

print()

# REPEATED NUMBER PYRAMID INVERTED - 1

def repeated_number_pyramid_inverted1(n):
    for j in range(n,0,-1):
        print(' ' *(n - j) + str(j) * (2 * j - 1))
repeated_number_pyramid_inverted1(5)

print()

# REPEATED NUMBER PYRAMID INVERTED - 2

def repeated_number_pyramid_inverted2(n):
    count=1
    for j in range(n,0,-1):
        print(' ' *(n - j) + str(count) * (2 * j - 1))
        count+=1
repeated_number_pyramid_inverted2(5)
