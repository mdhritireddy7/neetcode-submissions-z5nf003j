class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = Counter(nums)
        freq = [[] for i in range(len(nums)+1)] # index -> count & value -> [num]

        for n, c in count_nums.items():
            freq[c].append(n)

        result = []

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
        
        