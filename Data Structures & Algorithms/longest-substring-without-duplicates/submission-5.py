class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        substring = set()
        max_count = 0

        if len(s) == 1:
            return 1

        for r in range(len(s)):
            while s[r] in substring:
                substring.remove(s[l])
                l+=1
            substring.add(s[r])
            max_count = max(max_count, len(substring))
            

        return max_count

        