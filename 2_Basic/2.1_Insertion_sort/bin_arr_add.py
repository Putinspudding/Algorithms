#P12 2.1-4
def bin_add(a: list, b: list) -> list:
    i = len(a) - 1
    c = [0] * (i + 2)
    while (i >= 0):
        c[i + 1] = a[i] + b[i] + c[i + 1]
        if c[i + 1] >= 2:
            c[i + 1] = c[i + 1] - 2
            c[i] = c[i] + 1
        i = i - 1
    return c


a = [1, 1, 1]
b = [0, 0, 1]
print(bin_add(a, b))
