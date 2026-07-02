# SQUARE PATTERN
n=5
for i in range(n+1):
    print(n * '*')

print()

# SQUARE BORDER PATTERN
n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
