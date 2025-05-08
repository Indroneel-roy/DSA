# Problem Link : https://leetcode.com/problems/median-of-two-sorted-arrays/description/
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x, y = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(x) > len(y): # We have to start from sort len nums1 to avoid out of range
            x, y = y, x

        l, r = 0, len(x) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
            
            #add both nums before and after start -infinity and infinity to get right value
            Xleft = x[i] if i >= 0 else float('-infinity')
            Xright = x[i + 1] if (i+1) < len(x) else float('infinity')
            Yleft = y[j] if j >= 0 else float('-infinity')
            Yright = y[j + 1] if (j + 1) < len(y) else float('infinity')

            if Xleft <= Yright and Yleft <= Xright: # Checking left half and right half is right order
                if total % 2:
                    return min(Xright, Yright)
                else:
                    return (max(Xleft, Yleft) + min(Xright, Yright)) / 2
            elif Xleft > Yright: # this condition then we have to squeeze left portion of X
                r = i - 1
            else:
                l = i + 1                
if __name__ == "__main__":
    nums1 = [1,2]
    nums2 = [3,4]
    sol = Solution()
    res = sol.findMedianSortedArrays(nums1, nums2)
    print(res)