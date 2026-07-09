class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        arr = [0] * len(nums)
        n=len(nums)
        k = 0
        i = 0
        while i < len(nums):
            if nums[i]!=val:
                k=k+1
                i=i+1
            else:
                nums.pop(i)
        return k
            
            


        