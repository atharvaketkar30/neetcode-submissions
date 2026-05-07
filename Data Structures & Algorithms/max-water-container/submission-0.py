class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        r = 0

        for l in range(len(heights)):
            r = l + 1
            while r < len(heights):
                width = r - l
                water = min(heights[l], heights[r]) * width
                max_water = max(max_water, water)
                # print(water, max_water)
                r += 1

        return max_water