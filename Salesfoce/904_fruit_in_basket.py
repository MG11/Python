class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left, right = 0, 0
        fruitData = {} # key: index
        maxsize = 0
        while right < len(fruits):
            if len(fruitData) < 2 or (len(fruitData) == 2 and fruits[right] in fruitData):
                fruitData[fruits[right]] = right
                right += 1
            else:
                maxsize = max(right - left, maxsize)
                # del key from fruitData having min index
                # left = min index + 1
                f = min(fruitData, key = fruitData.get)
                left = fruitData[f] + 1
                del fruitData[f]
                fruitData[fruits[right]] = right
                right += 1

        maxsize = max(right - left, maxsize)
        return maxsize


