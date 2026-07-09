# NORMAL ALPHABET PYRAMID PATTERN

def normal_alphabet_pyramid(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(' ',end = '')

        # ASCENDING ALPHABETS
        for j in range(i + 1):
            print(chr(65 + j),end = '')

        # DESCENDING ALPHABETS
        for j in range(i - 1,-1,-1):
            print(chr(65 + j),end = '')
        print()
normal_alphabet_pyramid(5)

print()

# NORMAL ALPHABET PYRAMID PATTERN INVERTED

def normal_alphabet_pyramid_inverted(n):
    for i in range(n):
        for j in range(i):
            print(' ',end='')

        # ASCENDING ALPHABETS
        for j in range(n - i):
            print(chr(65 + j),end = '')

        # DESCENDING ALPHABETS
        for j in range(n - i - 2,-1,-1):
            print(chr(65 + j),end = '')
        print()
normal_alphabet_pyramid_inverted(5)

