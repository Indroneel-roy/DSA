# problem link : https://leetcode.com/problems/reconstruct-itinerary/description/
from typing import List
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, des in sorted(tickets):
            graph[src].append(des)
        route = []
        def dfs(src):
            while graph[src]:
                new_src = graph[src].pop(0)
                dfs(new_src)
            route.append(src)
        dfs("JFK")
        return route[::-1]  
if __name__ == "__main__":
    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    sol = Solution()
    print(sol.findItinerary(tickets))