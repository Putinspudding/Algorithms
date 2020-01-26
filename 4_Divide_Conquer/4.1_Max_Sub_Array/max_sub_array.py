import math


def max_sub(l: list, left: int, right: int):
    mid = (left + right) // 2
    if left == right:
        return [left, right, l[left]]
    else:
        left_max = max_sub(l, left, mid)
        right_max = max_sub(l, mid + 1, right)
        cross_max = max_crossing_sub(l, left, right)
        if left_max[2] >= right_max[2] and left_max[2] >= cross_max[2]:
            return left_max
        else:
            if right_max[2] >= left_max[2] and right_max[2] >= cross_max[2]:
                return right_max
            else:
                return cross_max


def max_crossing_sub(l: list, left: int, right: int):
    mid = (left + right) // 2
    left_sum = -math.inf
    sum = 0
    max_left = mid
    for i in range(mid, left - 1, -1):
        sum = sum + l[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = -math.inf
    sum = 0
    max_right = mid + 1
    for j in range(mid + 1, right + 1):
        sum = sum + l[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return [max_left, max_right, left_sum + right_sum]


def find_max_sub(l: list):
    return max_sub(l, 0, len(l) - 1)


a = [5, -1, 5, 2, 4, -1, 3]
print(find_max_sub(a))
