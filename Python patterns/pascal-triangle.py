n = 5
for i in range(n):
    print(' ' * (n - i), end='')
    val = 1
    for j in range(i + 1):
        print(f'{val} ', end='')
        val = val * (i - j) // (j + 1)
    print()
