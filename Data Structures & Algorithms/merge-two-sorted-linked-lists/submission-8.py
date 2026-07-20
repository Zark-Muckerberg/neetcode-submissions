# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = list1
        two_ptr = list2
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        #initialise an empty ListNode
        dummy = ListNode()
        tail = dummy

        #while current is not null
        while curr and two_ptr:

            #if value of node in list1 lesser or equal to node in list2, point to list2 node
            if curr.val <= two_ptr.val:
                #attach tail to current node
                tail.next = curr
                #increment curr
                curr = curr.next
            #value of list2 smaller than that of lis1
            else:
                #assign tail to point at list2 node
                tail.next=two_ptr
                #return two_ptr to point at next node in list2
                two_ptr = two_ptr.next
            
            #advance tail to most recent node
            tail=tail.next
        
        #if one linked list still has nodes
        if curr:
            tail.next = curr
        else:
            tail.next= two_ptr

        return dummy.next




            