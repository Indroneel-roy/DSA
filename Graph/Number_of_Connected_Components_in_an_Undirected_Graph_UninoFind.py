class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1]*n
        def find(n1):
            if par[n1] != n1:
                return find(par[n1])
            else: return n1
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            elif rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1
        res = n
        for n1, n2 in edges:
            res -= union(n1,n2)
        return res           
