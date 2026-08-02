# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #result array
        res = []
        curr = root
        #queue to do BFS
        queue = collections.deque()
        queue.append(curr)
        
        while queue:
            #stack to store right side view FOR EACH LEVEL
            stack = []

            for i in range (len(queue)):
                #pop FIFO element in queue
                node = queue.popleft()
                #if node exists
                if node:
                    #append its children to the queue
                    queue.append(node.left)
                    queue.append(node.right)
                    #append the node value to the stack
                    stack.append(node.val)
            #once for loop exits, all nodes on the level have been processed, we only need the top-
            #most element in the stack
            if stack:
                res.append(stack.pop())
        
        return res