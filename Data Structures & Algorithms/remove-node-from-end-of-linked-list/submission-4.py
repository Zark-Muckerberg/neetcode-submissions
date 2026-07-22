# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #find length of linked list
        length=0
        curr = head
        while curr:
            curr=curr.next
            length = length+1
        #index of node to be removed
        k = length-n
         #handling of when node to be removed is head node
        if k==0:
            return head.next
        prev = None
        curr = head
        #increment curr to point at index of node to be removed
        for i in range(k):
            prev = curr
            curr = curr.next

        #if there is a node before and after the node to be removed
        if curr.next:
            temp = curr.next
            #break link between node to be removed and next node
            curr.next = None
            curr=temp
            #break the link between the prev node and node to be removed, attach to node beyond
            prev.next = curr
        else:
            #there is no node after the node to be removed, remove curr
            prev.next=None
        return head