# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr=head
        if(not head or (head and not head.next)):
            return 0
        while(curr):
            if(curr.val=='V'):
                return 1
            curr.val='V'
            curr=curr.next
        return 0
        