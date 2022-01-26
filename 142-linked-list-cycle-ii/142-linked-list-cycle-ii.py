# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        curr=head
        while(curr):
            if curr in arr:
                return curr
            arr.append(curr)
            curr=curr.next
        return None
        
        