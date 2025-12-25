from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        for item in range(1,len(nums)):
            if nums[item]!=nums[k-1]:
                nums[k]=nums[item]
                k+=1
        return k
    
print(Solution.removeDuplicates(self="",nums = [0,0,1,1,1,2,2,3,3,4]))