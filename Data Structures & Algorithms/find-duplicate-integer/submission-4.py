class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #treat it like a linked list qn, number in array will be the index we go to
        #initialise 2 ptrs fast and slow, at zero
        slow =0
        fast =0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            #once slow and fast meet, break the loop
            if slow == fast:
                break

        #the meeting point is not necessarily the duplicate, it just detects the cycle
        #initalise another slow pointer
        slow2=0

        while True:
            slow2=nums[slow2]
            slow=nums[slow]
            if slow == slow2:
                return slow
        



        