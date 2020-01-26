def merge_sort(l: list, left: int, right: int):
    if left == right:
        return
    mid = (left + right) // 2
    merge_sort(l, left, mid)
    merge_sort(l, mid + 1, right)
    merge(l, left, mid, right)


def merge(l: list, left: int, mid: int, right: int):
    sorted = []
    i = left
    j = mid + 1
    while i <= mid or j <= right:
        if l[i] <= l[j]:
            sorted.append(l[i])
            i = i + 1
            if i > mid:
                for elements in range(j, right + 1):
                    sorted.append(l[elements])
                break
            continue
        if l[i] > l[j]:
            sorted.append(l[j])
            j = j + 1
            if j > right:
                for elements in range(i, mid + 1):
                    sorted.append(l[elements])
                break

    for numbers in range(left, right + 1):
        l[numbers] = sorted[numbers - left]


def sort(l: list):
    merge_sort(l, 0, len(l) - 1)


a = [5, 0, 12, 20, 7, 9, 10, 18, 5, -1]
sort(a)
print(a)


'''
The answer is:[-1, 0, 5, 5, 7, 9, 10, 12, 18, 20]
'''
