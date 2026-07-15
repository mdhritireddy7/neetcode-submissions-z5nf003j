from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustCount = defaultdict(int)

        for src, dst in trust:
            trustCount[src] -= 1
            trustCount[dst] += 1

        for i in trustCount:
            if trustCount[i] == n-1:
                return i

        return -1

        