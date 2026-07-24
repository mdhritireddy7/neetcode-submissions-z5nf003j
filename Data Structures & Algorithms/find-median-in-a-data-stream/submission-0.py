import heapq

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # check if num is less than the values in self.large
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * self.small[0]
            heapq.heappush(self.large, val)
            heapq.heappop(self.small)

        # check if the diff b/w the size of self.small and self.large is less than 1
        if len(self.small) > len(self.large) + 1:
            val = -1 * self.small[0]
            heapq.heappush(self.large, val)
            heapq.heappop(self.small)
        
        if len(self.large) > len(self.small) + 1:
            val = self.large[0]
            heapq.heappush(self.small, -1 * val)
            heapq.heappop(self.large)

        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return ((-1 * self.small[0]) + self.large[0]) / 2
        
        