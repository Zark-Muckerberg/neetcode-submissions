# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #iterative method
        prev = None
        curr = head

        while curr:
            #temp variable to store pointer to next linked list
            temp = curr.next
            #reverse the direction of the pointer
            curr.next = prev
            #increment previous to point to current node
            prev = curr
            #current now points to the next non-reversed node
            curr = temp
    
        return prev