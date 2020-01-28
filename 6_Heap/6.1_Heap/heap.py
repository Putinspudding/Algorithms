import copy
import math


# 6.1堆类定义
class heap:
    def __init__(self, B: list):
        self.heap = copy.deepcopy(B)
        self.size = len(B) - 1

    def left(self, i: int):
        return 2 * i

    def right(self, i: int):
        return 2 * i + 1

    def parent(self, i: int):
        return i // 2


# 6.2维持最大堆
def max_heapify(A: heap, i: int):
    left = A.left(i)
    right = A.right(i)
    if left <= A.size:
        if A.heap[left] > A.heap[i]:
            largest = left
        else:
            largest = i
    else:
        largest = i
    if right <= A.size:
        if A.heap[right] > A.heap[largest]:
            largest = right
    if not largest == i:
        temp = A.heap[largest]
        A.heap[largest] = A.heap[i]
        A.heap[i] = temp
        max_heapify(A, largest)


# 6.3建立最大堆
def build_max_heap(A: heap):
    for i in range(A.size // 2, 0, -1):
        max_heapify(A, i)


# 6.4堆排序
def heapsort(A: heap):
    build_max_heap(A)
    for i in range(A.size, 1, -1):
        temp = A.heap[1]
        A.heap[1] = A.heap[i]
        A.heap[i] = temp
        A.size = A.size - 1
        max_heapify(A, 1)


# 6.5优先队列
# 此时的堆都是最大堆
# 查找最大值
def heap_maximun(A: heap):
    return A.heap[1]


# 对最大值进行取出操作
def pop(A: heap):
    max = A.heap[1]
    A.heap[1] = A.heap[A.size]
    A.heap[A.size] = max
    A.size = A.size - 1
    max_heapify(A, 1)
    return max

#对某键值进行增加操作
def add_key_value(A: heap, num: int, value: int):
    if A.heap[num] < value:
        A.heap[num] = value
        while A.heap[num] > A.heap[A.parent(num)]:
            temp = A.heap[num]
            A.heap[num] = A.heap[A.parent(num)]
            A.heap[A.parent(num)] = temp
            num = A.parent(num)
            if num == 1:
                break


#对堆进行插入元素
def insert(A:heap,element:int):
    A.size = A.size+1
    A.heap.append(-math.inf)
    add_key_value(A,A.size,element)



a = [0, 16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
b = heap(a)
max_heapify(b, 2)
print(b.heap)
c = [0, 4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
d = heap(c)
build_max_heap(d)
print(d.heap)
add_key_value(d, 9, 15)
print(d.heap)
# heapsort(d)
# print(d.heap)
print(pop(d))
print(d.heap)
f = [0, 16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
g = heap(f)
insert(g,20)
print(g.heap)