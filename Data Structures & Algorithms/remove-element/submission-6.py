class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        i = 0
        while i < n:
            if nums[i]==val:
                n=n-1
                nums[i]=nums[n]

            else:
                i=i+1
        return n
            
            


        