class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj = { i:[] for i in range(n)}

        for ni, nj in edges:
            adj[ni].append(nj)
            adj[nj].append(ni)

        visited = set()
        def dfs(i, prev):
            if i in visited:
                return False

            visited.add(i)

            for j in adj[i]:
                if j == prev:
                    continue

                if not dfs(j, i):
                    return False

            return True
        
        return dfs(0, -1) and len(visited) == n

        