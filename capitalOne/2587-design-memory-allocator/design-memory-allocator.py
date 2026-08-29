class Allocator:

    def __init__(self, n: int):
        self.mem = [-1]*n
        self.blocks = defaultdict(list)
        

    def allocate(self, size: int, mID: int) -> int:
        cnt = 0

        for i in range(len(self.mem)):
            if self.mem[i] == -1:
                cnt += 1
            else:
                cnt = 0
            if cnt == size:
                start_index = i - cnt + 1
                self.mem[start_index: start_index + cnt] = [mID]*cnt
                self.blocks[mID].extend(list(range(start_index, i + 1)))
                return start_index
        return -1


    def freeMemory(self, mID: int) -> int:
        size = len(self.blocks.get(mID, []))
        for i in self.blocks.get(mID, []):
            self.mem[i] = -1
        self.blocks[mID] = []
        return size
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)