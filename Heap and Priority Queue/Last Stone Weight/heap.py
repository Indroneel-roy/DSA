#problem Link : https://leetcode.com/problems/last-stone-weight/
import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert to negative values for max heap simulation
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            # Pop two heaviest stones (most negative values)
            first = heapq.heappop(stones)   # heaviest stone (most negative)
            second = heapq.heappop(stones)  # second heaviest stone
            
            # If stones have different weights, push back the difference
            if first != second:  # since we're using negative values
                heapq.heappush(stones, first - second)
        
        # Return the last stone's weight, or 0 if no stones left
        return -stones[0] if stones else 0

# Test the solution
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: [2,7,4,1,8,1]
    stones1 = [2,7,4,1,8,1]
    result1 = sol.lastStoneWeight(stones1)
    print(f"Input: {[2,7,4,1,8,1]}")
    print(f"Output: {result1}")
    print(f"Expected: 1\n")