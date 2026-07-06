# HOLLOW RHOMBUS PATTERN

def hollow_rhombus(n):
    for i in range(1,(n+1)):
        if i==1 or i==n:
            print(' '*(n-i)+'*'*n)
        else:
            print(' '*(n-i)+'*'+' '*(n-2)+'*')
hollow_rhombus(5)
