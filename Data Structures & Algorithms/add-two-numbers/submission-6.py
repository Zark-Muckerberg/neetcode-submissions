# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result1 = 0
        result2 = 0
        curr1 = l1
        n=1
    
        while curr1:
            result1 = result1 + (curr1.val * n)
            n = n*10
            curr1 = curr1.next

        curr2 = l2
        n=1
        while curr2:
            result2 = result2 + (curr2.val * n)
            n = n*10
            curr2 = curr2.next

        total = result1+result2
        dummy = ListNode()
        curr = dummy
        if total == 0:
            curr.next = ListNode(0)
            return dummy.next
            
        while total != 0:
            curr.next = ListNode(total % 10)
            total = total//10
            curr=curr.next
        
        return dummy.next
        