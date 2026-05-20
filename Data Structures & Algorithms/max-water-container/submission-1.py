class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            maxA = min(heights[l], heights[r]) * (r - l)
            res = max(res, maxA)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res