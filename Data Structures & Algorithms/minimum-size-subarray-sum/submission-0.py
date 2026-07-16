class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        total=0
        length = float("inf")

        for r in range(len(nums)):
            total = total + nums[r]
            #once total is equal to or exceeds target, we decrement the window
            while total >= target:
                #once total hits or exceeds target, take the length of the current window
                length = min(length,r-l+1)

                #reduce the total
                total = total-nums[l]
                #decrement the window length
                l = l+1
        
        if length == float("inf"):
            return 0
        else:
            return length


