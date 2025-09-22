# problem Link : https://leetcode.com/problems/search-insert-position/
from typing import List
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
pick = 6   # hidden number (like in LeetCode)

def guess(num: int) -> int:
    if num == pick:
        return 0
    elif num > pick:
        return -1
    else:
        return 1

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = (l + r) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                r = mid - 1
            else:
                l = mid + 1        
if __name__ == "__main__":
    obj = Solution()
    print(obj.guessNumber(10)) # return 6
    print(obj.guessNumber(1))  # return 1
    pick = 1
    print(obj.guessNumber(2))  # return 1                
        