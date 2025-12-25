from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict={}
        for key,val in enumerate(nums):
            if target-val==my_dict:
                return [key,my_dict.get(target-val)]
            my_dict[val]=key
            
print(Solution.twoSum(self="",nums = [2,7,11,15], target = 9))
            