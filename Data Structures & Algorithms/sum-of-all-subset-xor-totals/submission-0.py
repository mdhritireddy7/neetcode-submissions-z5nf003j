class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.total = 0
        def dfs(index, curr_xor):
            if index == len(nums):
                self.total += curr_xor
                return 

            dfs(index+1, curr_xor)
            dfs(index+1, curr_xor^nums[index])

        dfs(0, 0)
        return self.total