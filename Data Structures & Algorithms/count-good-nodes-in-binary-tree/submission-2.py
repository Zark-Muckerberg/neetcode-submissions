# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node,maxVal):
            if not node:
                return 0
            #if current node val is greater than the maxVal seen so far
            if node.val >= maxVal:
                res=1
            else:
                res = 0
            #update maxVal for each new node visited
            maxVal = max(maxVal,node.val)
            res = dfs(node.left,maxVal) + res
            res = dfs(node.right,maxVal) + res
            return res
        
        return dfs(root,root.val)