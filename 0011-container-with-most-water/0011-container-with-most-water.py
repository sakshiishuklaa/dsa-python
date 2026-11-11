class Solution:
    def maxArea(self, height: list[int]) -> int:
        left=0
        right=len(height)-1
        calc=0
        
        while left<right:
            area=(right-left)*min(height[right],height[left])
            if height[left]<height[right]:
                left=left+1
            else:
                right=right-1
            calc=max(calc,area)
        return calc