# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
        
            left = dfs(node.left)
            #if there is an imbalanced subtree on the left side, return -1 straight away
            if left == -1:
                return -1

            #if there is an imbalanced subtree on the right side, return -1 straight away
            right = dfs(node.right)
            if right == -1:
                return -1
            
            #calculate the difference in height
            if abs(left - right) >1:
                return -1
            
            #return the height
            return 1+ max(left,right)
        
        return dfs(root) != -1

                
        