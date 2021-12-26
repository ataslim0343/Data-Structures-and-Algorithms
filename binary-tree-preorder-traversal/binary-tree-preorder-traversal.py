# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,resultlist):
        if(root==None):
            return
        else:
            resultlist.append(root.val)
            self.dfs(root.left,resultlist)
            self.dfs(root.right,resultlist)
            
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        resultlist=[]
        self.dfs(root,resultlist)
        return resultlist
    
            
        
        
        