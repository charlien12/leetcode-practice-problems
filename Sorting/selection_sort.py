from typing import List
class Solution:
    def selection_sort(self,nums:List[int])->List[int]:
        n=len(nums)
        for i in range(n-1):
            sidx=i
            for j in range(i+1,n):
                if nums[j]<nums[sidx]:
                    sidx=j
            nums[i],nums[sidx]=nums[sidx],nums[i]
        return nums
    
print(Solution.selection_sort(self="",nums=[4,5,3,2,1]))