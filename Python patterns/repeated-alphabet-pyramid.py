# REPEATED ALPHABET PYRAMID

def repeated_alphabet_pyramid(n):
    count = 65
    for i in range(1,(n + 1)):
        print(' ' * (n - i) + chr(count) * (2 * i - 1))
        count += 1
repeated_alphabet_pyramid(5)

print()

# REPEATED ALPHABET PYRAMID INVERTED

def repeated_alphabet_pyramid_inverted(n):
    count = 65
    for i in range(n,0,-1):
        print(' ' * (n - i) + chr(count) * (2 * i - 1))
        count += 1
repeated_alphabet_pyramid_inverted(5)
