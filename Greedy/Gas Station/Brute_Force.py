from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(len(gas)):
            tank = gas[i] - cost[i]
            if tank < 0:
                continue
            j = (i+1) % n 
            
            while j != i:
                tank += gas[j]
                tank -+ cost[j]
                if tank < 0:
                    break
                j += 1
                j %= n
            if j == i:
                return i
        return -1

if __name__ == "__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]   
    s = Solution()
    print(s.canCompleteCircuit(gas, cost))                
            