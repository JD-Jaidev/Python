# FLOYD'S TRIANGLE

def floyd_triangle(n):
    num = 1
    for i in range(1,n):
        for j in range(i):
            print(str(num) + ' ',end = '')
            num += 1
        print()
floyd_triangle(5)
