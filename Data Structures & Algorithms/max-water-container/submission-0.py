class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            if heights[l] < heights[r]:
                area = heights[l] * (r-l)
                max_area = max(area, max_area)
                l += 1
            elif heights[l] > heights[r]:
                area = heights[r] * (r-l)
                max_area = max(area, max_area)
                r -= 1
            else:
                area = heights[l] * (r-l)
                max_area = max(area, max_area)
                l += 1

        return max_area


        