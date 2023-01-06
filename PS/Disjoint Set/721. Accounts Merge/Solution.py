from typing import List
from collections import defaultdict
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
    
    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.root[root_y] = root_x
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        ownership = {}

        for idx, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(ownership[email], idx)
                ownership[email] = idx
        
        ans = defaultdict(list)
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email)
        
        return [[accounts[i][0], *sorted(emails)] for i, emails in ans.items()]