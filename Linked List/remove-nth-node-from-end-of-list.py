#https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=problem-list-v2&envId=linked-list
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        first_ptr=second_ptr=dummy
        for item in range(n):
            second_ptr=second_ptr.next
        while second_ptr.next:
            first_ptr=first_ptr.next
            second_ptr=second_ptr.next
        first_ptr.next=first_ptr.next.next
        return dummy.next