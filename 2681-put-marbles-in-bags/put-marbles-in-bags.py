# https://www.youtube.com/watch?v=lB_gLotpnuY

class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        if k == 1:
            return 0
        splits = []
        for i in range(len(weights) - 1):
            splits.append(weights[i] + weights[i + 1])

        splits.sort()
        print(splits)
        i = k - 1
        min_score = sum(splits[:i])
        max_score = sum(splits[ -i:])
        return max_score - min_score
    