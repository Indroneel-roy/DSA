# Problem Link : https://leetcode.com/problems/combination-sum-ii/description/
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort the input to handle duplicates easily and ensure combinations are in order
        candidates.sort()

        res = []   # Final result list to store all unique combinations
        curr = []  # Current combination being built (used in backtracking)

        # Helper function for backtracking
        def backtrack(curr, pos, target):
            # If the target becomes 0, we've found a valid combination
            if target == 0:
                res.append(curr.copy())  # Add a copy of current combination to the result
                return
            # If the target goes below zero, this path is invalid
            elif target < 0:
                return

            prev = -1  # Used to skip duplicates at the same recursive depth
            for i in range(pos, len(candidates)):
                # Skip duplicates: if current value is same as previous at same level, skip it
                if candidates[i] == prev:
                    continue

                # Choose the current candidate
                curr.append(candidates[i])
                # Recurse with updated target and move to the next index (i + 1) since each element can be used once
                backtrack(curr, i + 1, target - candidates[i])
                # Backtrack: remove the last chosen element before trying next option
                curr.pop()
                # Mark current value as previous so duplicates can be skipped in next iterations
                prev = candidates[i]

        # Initial call to backtracking with an empty combination starting from index 0
        backtrack([], 0, target)

        # Return all unique combinations found
        return res
if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    target = 8
    sol = Solution()
    print(sol.combinationSum2(candidates, target))