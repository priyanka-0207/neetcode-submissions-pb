class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) -1
        max_count = 0
        while i < j:
            area = min(heights[j], heights[i]) * (j - i) 
            max_count = max(max_count, area) 
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_count

