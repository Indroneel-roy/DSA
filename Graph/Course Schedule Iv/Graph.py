# problem link : https://leetcode.com/problems/course-schedule-iv/
from typing import List
from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for preq, crs in prerequisites:
            adj[crs].append(preq)
        prereqMap = {}
        def dfs(crs):
            
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for prereq in adj[crs]:
                    prereqMap[crs] |= dfs(prereq)
                prereqMap[crs].add(crs)
            return prereqMap[crs]
        for crs in range(numCourses):
            dfs(crs)
        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])
        return res    

if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1,0]]
    queries = [[0,1],[1,0]]
    sol = Solution()
    print(sol.checkIfPrerequisite(numCourses, prerequisites, queries))