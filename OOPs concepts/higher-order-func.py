def divisor(x):
    def dividend(y):
        return y / x
    return dividend

div = divisor(2)
print(div(10))