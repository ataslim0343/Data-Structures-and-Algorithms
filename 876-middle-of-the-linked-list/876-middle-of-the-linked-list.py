# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node=head
        n=0
        while(head):
            n+=1
            head=head.next
        print(n)
        if(n%2==0):
            p=n//2
            while(p):
                node=node.next
                p-=1
            return node
        else:
            p=(n//2)+1
            while(p-1):
                node=node.next
                p-=1
            return node
        
        