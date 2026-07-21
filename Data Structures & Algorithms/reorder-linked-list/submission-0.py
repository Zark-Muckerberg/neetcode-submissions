# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #brute force
        #append nodes to an array
        curr = head
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        i=0
        j=len(nodes)-1
        while i <j:
            nodes[i].next = nodes[j]
            i=i+1
            #once i and j meet, break to prevent loop
            if i>=j:
                break
            nodes[j].next = nodes[i]
            j=j-1
        #once loop terminates, i is at the last node of the new linked list
        nodes[i].next = None