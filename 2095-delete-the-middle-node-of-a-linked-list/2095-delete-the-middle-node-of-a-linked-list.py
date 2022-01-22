# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        dummy.next=head
        fast=slow=head
        
#Handling Edge Cases
        if(head and not head.next):
            return None
        
#Using Concept for slow & fats pointer. dummy pointer will tell the prev on middle node
        while(fast and fast.next):
            dummy=slow
            slow=slow.next
            fast=fast.next.next
            
        dummy.next=slow.next
        return head
        