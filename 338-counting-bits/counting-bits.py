class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0]*(n+1)
        twopower = 0
        for i in range(n+1):
            biton = 2**twopower
            if i == 2**twopower:
                output[i] = 1
                twopower += 1
            else:
                previouspower = int(biton/2)
                output[i] = output[previouspower] + output[i - previouspower]
        return output
