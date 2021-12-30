/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> postorderTraversal(TreeNode root) 
    {
        List<Integer> reslist= new ArrayList<Integer>();
        dfs(root,reslist);
        return reslist;
    }
    public void dfs(TreeNode root,List<Integer> reslist)
    {
        if(root==null)
        {
            return;
        }
        dfs(root.left,reslist);
        dfs(root.right,reslist);
        reslist.add(root.val);
    }
}