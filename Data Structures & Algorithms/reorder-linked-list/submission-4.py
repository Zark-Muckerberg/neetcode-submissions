# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #reverse the linked list starting from the halfway mark

        slow = head
        fast = head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #slow is at the mid point, slow.next is the start of the halfway mark
        second_ptr = slow.next

        #slow is at the mid point, fast is at the end, break the link in the middle
        slow.next = None
        prev = None
        #reverse starting from the midway point
        while second_ptr:
            temp = second_ptr.next
            second_ptr.next = prev
            prev = second_ptr
            second_ptr = temp
         #merge the 2 lists

        #prev will be the head of the 2nd list
        second_ptr = prev
        first = head
        while second_ptr:
            temp1 = first.next
            temp2 = second_ptr.next
            first.next = second_ptr
            second_ptr.next = temp1
            first = temp1
            second_ptr = temp2
