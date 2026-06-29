# RIGHT TRIANGLE PATTERN
n=5
for i in range(1,n+1):
    print(i*'*')

print()

# RIGHT TRIANGLE PATTERN INVERTED
n=5
for i in range(n,0,-1):
    print(i*'*')

print()

# RIGHT TRIANGLE USING NUMBERS - 1

for i in range(1,6):
    print(str(i) * i)

print()

# RIGHT TRIANGLE USING NUMBERS - 2
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()

