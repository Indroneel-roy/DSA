# problem link : https://leetcode.com/problems/accounts-merge/description/
from typing import List
from collections import defaultdict
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.find(self.par[x])
            x = self.par[x]
        return x
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True                       
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {}
        for i, a in enumerate(accounts):
            for e in a[1 : ]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i
        GroupEmail = defaultdict(list)
        for e, i in emailToAcc.items():
            leader = uf.find(i)
            GroupEmail[leader].append(e)
        res = []
        for i, emails in GroupEmail.items():
            name = accounts[i][0]
            res.append([name] + sorted(GroupEmail[i])) 
        return res      
if __name__ == "__main__":
    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    sol = Solution()
    print(sol.accountsMerge(accounts))       
