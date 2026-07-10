class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        candidates.sort()

        def dfs(index, curr_sum, path):
            if curr_sum > target:
                return 

            if index == len(candidates):
                if curr_sum == target:
                    self.result.append(path[:])
                return

            next_index = index
            while next_index + 1 < len(candidates) and candidates[next_index] == candidates[next_index + 1]:
                next_index += 1

            dfs(next_index+1, curr_sum, path)

            path.append(candidates[index])
            dfs(index+1, curr_sum + candidates[index], path)
            path.pop()

        dfs(0, 0, [])
        return self.result
        