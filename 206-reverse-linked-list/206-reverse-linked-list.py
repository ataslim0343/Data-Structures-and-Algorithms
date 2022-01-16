# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Time=O(n)
# Space=O(n)

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
#------------------Approach 1-----------------------#


        # arr=[]
        # node = head
        # temp=head
        # while(node):
        #     arr.append(node.val)
        #     node=node.next
        # for i in range(len(arr)-1,-1,-1):
        #     temp.val=arr[i]
        #     temp=temp.next
        # return head


#------------------Approach 2-----------------------#

        curr=head
        prev=None
        while(curr!=None):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev

        