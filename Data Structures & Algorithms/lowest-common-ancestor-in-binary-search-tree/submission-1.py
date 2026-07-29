# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if not root or not p or not q:
            return None
        
        #both p and q lie in the left subtree, LCA must be further down the left subtree
        if max(p.val,q.val) < root.val:
            #recursiveely pass in root.left as new root for LCA function
            return self.lowestCommonAncestor(root.left,p,q)
        #both p and q lie in the right subtree, LCA must be further down the right subtree
        elif min(p.val,q.val) > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        #p and q are on opposite sides, current root is the LCA OR p/q IS the root
        else:
            return root
            

        