from collections import defaultdict


class Allocator:
    def __init__(self, n: int):
        self.n = n
        self.used = defaultdict(int)
        self.free = []

    def allocate(self, size: int, mID: int) -> int:
        if size <= 0:
            return -1
        for i in range(self.n - size + 1):
            if all((i + j) not in self.used for j in range(size)):
                for j in range(size):
                    self.used[i + j] = mID
                return i
        return -1

    def free(self, mID: int) -> int:
        removed = 0
        for key, val in list(self.used.items()):
            if val == mID:
                del self.used[key]
                removed += 1
        return removed
