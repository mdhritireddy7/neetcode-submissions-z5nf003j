class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxSequenceLen = 0


        for i in nums:
            if (i-1) not in nums:
                curr_num = i
                curr_len = 1
                while (curr_num + 1) in nums:
                    curr_len += 1
                    curr_num += 1
                maxSequenceLen = max(maxSequenceLen, curr_len)

        return maxSequenceLen
        