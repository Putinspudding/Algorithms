import insertion_sort


def bucket_sort(A: list):
    C = []
    length = len(A)
    B = [None] * length
    for i in range(length):
        B[i] = [None]
    for j in A:
        if B[int((length * j) // 1)] == [None]:
            B[int((length * j) // 1)] = [j]
        else:
            B[int((length * j) // 1)].append(j)
    for k in B:
        if not k == [0]:
            insertion_sort.sort(k)
    for x in B:
        if x == [None]:
            continue
        C = C + x
    return C


a = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
b = bucket_sort(a)
print(b)
