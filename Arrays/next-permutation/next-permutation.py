from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=len(nums)-1
        while i>0 and nums[i-1]>=nums[i]:
            i-=1
        if i==0:
            nums.reverse()
            return
        j=len(nums)-1
        while j>=i and nums[j]<=nums[i-1]:
            j-=1
        nums[j],nums[i-1]=nums[i-1],nums[j]
        nums[i:]=reversed(nums[i:])
print(Solution.nextPermutation(self="",nums = [1,1,5]))