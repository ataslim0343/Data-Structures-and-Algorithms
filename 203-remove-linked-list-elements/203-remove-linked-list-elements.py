# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(-1)
        temp=dummy
        dummy.next=head
        if head==None:
            return None
        while(temp!=None and temp.next!=None):
            if(temp.next.val==val):
                temp.next=temp.next.next
            else:
                temp=temp.next
        return dummy.next
        
        