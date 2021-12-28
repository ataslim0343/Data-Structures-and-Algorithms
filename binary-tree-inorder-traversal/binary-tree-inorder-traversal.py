# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        result=[]
        while(1):
            if(root):
                stack.append(root)
                root=root.left
            else:
                if(not stack):
                    break
                else:
                    root=stack.pop()
                    result.append(root.val)
                    root=root.right
        return result
        