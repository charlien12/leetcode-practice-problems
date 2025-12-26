from typing import List
class Solution:
    def bubble_sort(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n):
            for j in range(0,n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums
    
    def optimized_bubble_sort(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n):
            swapped = False
            for j in range(0,n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                    swapped = True
                if not swapped:
                    break
        return nums
    
print(Solution.bubble_sort(self="",nums=[5,4,3,2,1]))