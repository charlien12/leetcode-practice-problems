from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        low=max_area=0
        high=len(height)-1
        while low<=high:
            wt=high-low
            ht=min(height[low],height[high])
            curr_area=ht*wt
            max_area=max(max_area,curr_area)
            if height[low]<height[high]:
                low+=1
            else:
                high-=1
        return max_area