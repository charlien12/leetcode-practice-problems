#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=problem-list-v2&envId=string

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set=set()
        left=max_length=0
        for item in range(len(s)):
            while s[item] in my_set:
                my_set.remove(s[left])
                left+=1
            my_set.add(s[item])
            max_length=max(max_length,item-left+1)
        return max_length