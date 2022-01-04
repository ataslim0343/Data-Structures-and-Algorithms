# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        s=""
        node=head
        while(node):
            s+=str(node.val)
            node=node.next
        return int(s,2)
        