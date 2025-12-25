from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre_element=strs[0]
        n=len(pre_element)
        for item in strs[1:]:
            while pre_element!=item[0:n]:
                n-=1
                if n==0:
                    return ""
                pre_element=pre_element[0:n]
        return pre_element
    
print(Solution.longestCommonPrefix(self="",strs = ["flower","flow","flight"]))