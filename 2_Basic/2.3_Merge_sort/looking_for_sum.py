#P22 2.3-7
def search(s: set, x: int) -> set:
    for i in s:
        if x - i in s and not x-i==i:
            return {i, x - i}


sample = {1, 2, 3, 4, 5, 6, 7}
print(search(sample, 5))
