# A中数值都<=k
def counting_sort(A: list, k: int):
    B = [0] * (len(A) + 1)
    C = [0] * (k + 1)
    for i in A:
        C[i] = C[i] + 1
    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1
    B.pop(0)
    return B


A = [1, 8, 3, 4, 10, 4]
print(counting_sort(A, 10))
