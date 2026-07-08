# NORMAL ALPHABET TRIANGLE

def alphabet_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            print(chr(65 + j),end = '')
        print()
alphabet_triangle(5)

print()

# NORMAL ALPHABET TRIANGLE INVERTED

def alphabet_triangle_inverted(n):
    for i in range((n - 1),-1,-1):
        for j in range(i + 1):
            print(chr(65 + j),end = '')
        print() 
alphabet_triangle_inverted(5)

