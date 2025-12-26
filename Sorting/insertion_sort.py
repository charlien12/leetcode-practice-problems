from typing import List
class Solution:
    def insertion_sort(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(1,n):
            curr=i
            prev=i-1
            while(prev>=0 and nums[prev]>curr):
                nums[prev+1]=nums[prev]
                prev-=1
            nums[prev+1]=curr
        return nums
    
print(Solution.insertion_sort(self="",nums=[5,4,3,2,1]))