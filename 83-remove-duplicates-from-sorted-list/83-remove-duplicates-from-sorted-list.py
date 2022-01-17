# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node=head
        while node!=None and node.next!=None:
            if(node.val==node.next.val):
                node.next=node.next.next
            else:
                node=node.next
        return head
        