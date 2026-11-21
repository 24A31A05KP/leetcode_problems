
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        adj = [[] for _ in range(n)]

        for i in range(1, n):
            adj[parent[i]].append(i)

        new_parent = parent[:]
        last = {}

        def dfs(node):
            ch = s[node]

            old = last.get(ch, -1)

            if old != -1:
                new_parent[node] = old

            last[ch] = node

            for child in adj[node]:
                dfs(child)

            if old == -1:
                last.pop(ch, None)
            else:
                last[ch] = old

        dfs(0)

        new_adj = [[] for _ in range(n)]

        for i in range(1, n):
            new_adj[new_parent[i]].append(i)

        ans = [0] * n

        def calculate(node):
            ans[node] = 1

            for child in new_adj[node]:
                ans[node] += calculate(child)

            return ans[node]

        calculate(0)

        return ans