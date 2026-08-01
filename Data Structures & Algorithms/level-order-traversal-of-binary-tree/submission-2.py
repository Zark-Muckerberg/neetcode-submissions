# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #result array
        res = []
        curr = root
        queue = collections.deque()
        queue.append(curr)

        #while queue not empty
        while queue:
            #list to store the nodes FOR EACH LEVEL
            level =[]
            for i in range(len(queue)):
                #pop nodes from left of the queue
                node = queue.popleft()
                #check for node is NULL
                if node:
                    #if not null, we append the val of node to the level
                    level.append(node.val)
                    #append the CHILDREN of the node to the queue
                    queue.append(node.left)
                    queue.append(node.right)
            
            #once for loop completes, all node values of that level are in level array
            #append to result array
            if level:
                res.append(level)

        return res

        