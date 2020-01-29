import random
import quicksort


def randomize(A: list, begin: int, end: int):
    number = random.randint(begin, end)
    A[number], A[end] = A[end], A[number]


def randomquicksort(A: list, begin: int, end: int):
    if end > begin:
        randomize(A, begin, end)
        compare = quicksort.partition(A, begin, end)
        randomquicksort(A, begin, compare - 1)
        randomquicksort(A, compare + 1, end)


a = [2, 8, 7, 1, 3, 5, 6, 4]
randomquicksort(a, 0, 7)
# print(a)
