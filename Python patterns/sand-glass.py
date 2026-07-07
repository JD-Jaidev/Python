# SAND GLASS PATTERN - 1

def sand_glass1(n):
    for i in range(n,1,-1):
        print(' ' * (n - i)+'*'*(2*i-1))
    for j in range(2,(n+1)):
        print(' ' * (n - j)+'*'*(2*j-1))
sand_glass1(5)

print()

# SAND GLASS PATTERN - 2

def sand_glass2(n):
    for i in range(n,0,-1):
        print(' ' * (n - i)+'*'*(2*i-1))
    for j in range(1,(n+1)):
        print(' ' * (n - j)+'*'*(2*j-1))
sand_glass2(5)
