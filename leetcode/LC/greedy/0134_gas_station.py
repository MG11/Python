# https://leetcode.com/problems/gas-station/
# refer alex xu book

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        netGas = [0] * len(gas)
        
        for i in range(len(gas)):
            netGas[i] = gas[i] - cost[i]
        
        tank = 0
        start = 0

        for i in range(len(gas)):
            tank += netGas[i]
            if tank < 0:
                start = i + 1
                tank = 0
        
        return start if tank >= 0 else -1
