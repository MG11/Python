class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = sorted([dist[i]/speed[i] for i in range(len(dist))])
        
        counter = 0
        for i in range(len(dist)):
            if time[i] > i:
                counter += 1
            else:
                return counter
        return counter