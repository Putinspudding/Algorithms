def sort(l: list) -> list:
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and key < l[j]:
            l[j + 1] = l[j]
            l[j] = key
            j = j - 1
    return l


def reverse_sort(l: list) -> list:
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and key > l[j]:
            l[j + 1] = l[j]
            l[j] = key
            j = j - 1
    return l


a = [6, 1, 3, 0, 2, 4, -1]
print(sort(a))
print(reverse_sort(a))
