class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []

        def backtracking(index, path):
            if index == len(nums):
                self.result.append(path[:])
                return 

            backtracking(index + 1, path)

            path.append(nums[index])
            backtracking(index + 1, path)
            path.pop()

        backtracking(0, [])
        return self.result
        