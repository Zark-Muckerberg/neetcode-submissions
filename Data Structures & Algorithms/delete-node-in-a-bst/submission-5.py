# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        curr = root
        #maintain a node to track previous node
        prev = None
        #find the node to delete
        while curr and curr.val != key:
            prev = curr

            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        if not curr:
            return root
        #node with one or no children
        if not curr.left or not curr.right:
            #if only left child
            if curr.left:
                child = curr.left
            #if only right child
            else:
                child = curr.right
            
            if not prev:
                return child
            elif prev.left == curr:
                prev.left = child
            else:
                prev.right = child
        else:
            #node with 2 children
            parent = None # parent of right subTree min node
            delNode = curr
            curr = curr.right

            while curr.left:
                parent = curr
                curr = curr.left
            
            if parent:
                parent.left = curr.right #if there was a left traversal
                curr.right = delNode.right
            
            curr.left = delNode.left

            if not prev:
                return curr
            
            if prev.left == delNode:
                prev.left = curr
            else:
                prev.right = curr
        return root

        