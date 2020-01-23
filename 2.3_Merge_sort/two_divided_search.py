#P22 2.3-5 二分查找算法
def two_divided(l: list, num: int, left: int, right: int) -> int:
    mid = (left + right) // 2
    if right - left <= 1:
        if num == l[left]:
            return left
        if num == l[right]:
            return right
        return None
    if l[mid] >= num:
        return two_divided(l, num, left, mid)
    else:
        return two_divided(l, num, mid, right)


def search(l: list, num: list) -> int:
    return two_divided(l, num, 0, len(l) - 1)


a = [0, 2, 4, 6, 8]
print(search(a, 6))
