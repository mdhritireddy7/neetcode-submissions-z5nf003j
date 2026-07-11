class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        nums.sort()

        def dfs(index, path):
            if index == len(nums):
                self.result.append(path[:])
                return 

            next_index = index
            while next_index + 1 < len(nums) and nums[next_index] == nums[next_index + 1]:
                next_index += 1
            dfs(next_index + 1, path)
            
            path.append(nums[index])
            dfs(index+1, path)
            path.pop()

        dfs(0, [])
        return self.result
        