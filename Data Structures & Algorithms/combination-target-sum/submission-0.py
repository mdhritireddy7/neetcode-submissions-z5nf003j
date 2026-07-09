class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.result = []

        def dfs(index, curr_sum, path):
            if curr_sum > target:
                return

            if index == len(nums):
                if curr_sum == target:
                    self.result.append(path[:])
                return 

            dfs(index+1, curr_sum, path)

            path.append(nums[index])
            dfs(index, curr_sum + nums[index], path)
            path.pop()

        dfs(0, 0, [])

        return self.result
        