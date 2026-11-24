class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left,right =0,len(heights)-1
        while left<right:
            width = right - left
            if heights[left] < heights[right]:
                area = heights[left] *width
                left+=1 
            else:
                area = heights[right]*width
                right-=1 
            
            max_area = max(area,max_area)
        return max_area