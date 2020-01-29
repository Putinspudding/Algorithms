def quicksort(A: list, begin: int, end: int):
    if end > begin:
        compare = partition(A, begin, end)
        quicksort(A, begin, compare - 1)
        quicksort(A, compare + 1, end)


def partition(A: list, begin: int, end: int):
    sample = A[end]
    i = begin - 1
    for j in range(begin, end):
        if A[j] <= sample:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[end] = A[end], A[i + 1]
    return i + 1


a = [2, 8, 7, 1, 3, 5, 6, 4]
quicksort(a, 0, 7)
print(a)
