# Problem Link : https://leetcode.com/problems/longest-happy-string/description/
import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res, maxHeap = '', []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))

        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break
                count2, char2 = heapq.heappop(maxHeap)
                res += char2
                count2 += 1
                if count2:
                    heapq.heappush(maxHeap, (count2, char2))
            else:
                res += char
                count += 1
            if count:
                heapq.heappush(maxHeap, (count, char))
        return res              
if __name__ == "__main__":
    obj = Solution()
    # Example 1
    a = 1
    b = 1
    c = 7
    print(obj.longestDiverseString(a, b, c)) # return "ccaccbcc"
    # Example 2
    a = 2
    b = 2
    c = 1
    print(obj.longestDiverseString(a, b, c)) # return "aabbc"
    # Example 3
    a = 7
    b = 1
    c = 0
    print(obj.longestDiverseString(a, b, c)) # return "aabaa"    