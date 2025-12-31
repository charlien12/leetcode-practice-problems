#https://leetcode.com/problems/validate-binary-search-tree/description/?envType=problem-list-v2&envId=binary-tree
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root,minimum,maximum):
            if not root:
                return
            if not(root.val>minimum and root.val<maximum):
                return False
            return valid(root.left,minimum,root.val) and valid(root.right,root.val,maximum)
        return valid(root,float("-inf"), float("inf"))