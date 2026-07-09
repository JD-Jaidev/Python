# CONTINUOUS ALPHABET PYRAMID PATTERN

def continuous_alphabet_pyramid(n):
    ch = 65
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")

        for j in range(2 * i + 1):
            print(chr(ch), end="")
            ch += 1
            if ch > 90:
                ch = 65
        print()
continuous_alphabet_pyramid(5)

print()

# CONTINUOUS ALPHABET PYRAMID PATTERN

def continuous_alphabet_pyramid_inverted(n):
    ch = 65
    for i in range(n):
        for j in range(i):
            print(" ", end="")

        for j in range(2 * (n - i) - 1):
            print(chr(ch), end="")
            ch += 1
        if ch > 90:
            ch = 65
        print()
continuous_alphabet_pyramid_inverted(5)

