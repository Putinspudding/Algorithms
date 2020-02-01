import random
def randomized_partition(A:list,begin:int,end:int):
    number = random.randint(begin, end)
    A[number], A[end] = A[end], A[number]
    sample = A[end]
    i = begin - 1
    for j in range(begin, end):
        if A[j] <= sample:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[end] = A[end], A[i + 1]
    return i + 1
    pass


def randomized_select(A:list,begin:int,end:int,loc:int):
    if begin == end :
        return A[begin]
    comparsion = randomized_partition(A,begin,end)
    present_loc = comparsion - begin + 1
    if loc == present_loc:
        return A[comparsion]
    elif loc<present_loc:
        return randomized_select(A,begin,comparsion-1,loc)
    else:
        return randomized_select(A,comparsion+1,end,loc-present_loc)


a = [1,3,2,5,9,4]
print(randomized_select(a,0,5,4))
