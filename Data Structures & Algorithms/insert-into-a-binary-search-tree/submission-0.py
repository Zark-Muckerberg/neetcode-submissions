# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #root empty, val becomes root
        if not root:
            return TreeNode(val)
        curr = root

        while True:

            if val < curr.val:
                #if curr.left is empty, insert val into curr.left
                if not curr.left:
                    curr.left = TreeNode(val)
                    #inserted, just return
                    return root
                #curr.left not empty, keep going further down the BST
                curr=curr.left
            elif val > curr.val:
                #if curr.right is empty, insert val into curr.right
                if not curr.right:
                    curr.right = TreeNode(val)
                    #inserted, just return
                    return root
                #curr.right not empty, keep going further down the BST
                curr=curr.right
                

        