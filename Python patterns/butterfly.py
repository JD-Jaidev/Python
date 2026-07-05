# BUTTERFLY PATTERN

n=5

# UPPER HALF
for i in range(1,(n+1)):
    print('*' * i + ' ' * (2 * (n-i)) + '*' * i)

# LOWER HALF
for j in range(n,0,-1):
    print('*' * j + ' ' * (2*(n-j)) + '*' * j)

