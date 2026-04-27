class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_l = height[l]
        max_r = height[r]
        total_water = 0

        while l < r:
            if max_l < max_r:
                l += 1
                water = min(max_l, max_r) - height[l]
                if water >= 0:
                    total_water += water
                max_l = max(max_l, height[l])
            elif max_l > max_r:
                r -= 1
                water = min(max_l, max_r) - height[r]
                if water >= 0:
                    total_water += water
                max_r = max(max_r, height[r])
            else:
                l += 1
                water = min(max_l, max_r) - height[l]
                if water >= 0:
                    total_water += water
                max_l = max(max_l, height[l])

        return total_water


                

        