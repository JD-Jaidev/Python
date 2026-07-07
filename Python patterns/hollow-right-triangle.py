# HOLLOW RIGHT TRIANGLE

def hollow_right_triangle(n):
    for i in range(1,(n+1)):
        if i==1 or i==2 or i==n:
            print('*'*i)
        else:
            print('*'+' '*(i-2)+'*')
hollow_right_triangle(5)

print()

# HOLLOW RIGHT TRIANGLE INVERTED

def hollow_right_triangle_inverted(n):
    for i in range(n,0,-1):
        if i==1 or i==2 or i==n:
            print('*'*i)
        else:
            print('*'+' '*(i-2)+'*')
hollow_right_triangle_inverted(5)
