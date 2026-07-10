class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []

        def dfs(num, path): 

            if k == len(path):
                self.result.append(path[:])
                return

            if num > n:
                return

            dfs(num+1, path)

            path.append(num)
            dfs(num+1, path)
            path.pop()

        dfs(1, [])

        return self.result

            

        