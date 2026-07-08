# CONTINUOUS RIGHT TRIANGLE

def continuous_right_triangle(n):
    current_char=65
    for i in range(1,(n+1)):
        for j in range(i):
            print(chr(current_char),end='')
            current_char+=1
        print()
continuous_right_triangle(5)

print()

# CONTINUOUS RIGHT TRIANGLE INVERTED

def continuous_right_triangle_inverted(n):
    current_char=65
    for i in range(n,0,-1):
        for j in range(i):
            print(chr(current_char),end='')
            current_char+=1
        print()
continuous_right_triangle_inverted(5)
