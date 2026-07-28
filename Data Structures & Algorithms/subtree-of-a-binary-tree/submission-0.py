# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #empty tree is alw a subtree
        if not subRoot:
            return True
        
        if not root:
            return False
        
        #check if root of tree and subtree are the  same
        if self.sameTree(root,subRoot):
            return True
        
        #recursively traverse the left and right subTrees of the main trees
        return(self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))
    
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #first recursive return returns true
        if not root and not subRoot:
            return True
        #we have found matching nodes, inspect the subtrees
        if root and subRoot and root.val==subRoot.val:
            #will only return True if both subTrees match
            return (self.sameTree(root.left,subRoot.left) and self.sameTree(root.right,subRoot.right))
        #the moment root.val != subTree.val, we do not enter the above condition and return False
        return False
        
