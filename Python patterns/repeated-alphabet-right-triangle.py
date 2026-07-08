# REPEATED ALPHABET RIGHT TRIANGLE

def repeated_alphabet_triangle(n):
    for i in range(0,n):
        for j in range(i + 1):
            print(chr(65 + i),end = '')
        print()
repeated_alphabet_triangle(5)

print()

# REPEATED ALPHABET RIGHT TRIANGLE INVERTED

def repeated_alphabet_triangle_inverted(n):
    for i in range(n - 1,-1,-1):
        for j in range(i + 1):
            print(chr(65 + i),end = '')
        print()
repeated_alphabet_triangle_inverted(5)
