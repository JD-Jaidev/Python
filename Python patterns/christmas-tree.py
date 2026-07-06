# CHRISTMAS TREE PATTERN

def christmas_tree(n):
    for i in range(1,(n+1)):
        print(' '*(n-i)+'*'*(2*i-1))
    for _ in range(2):
        print(' '*(n-1)+'*')
christmas_tree(5)
