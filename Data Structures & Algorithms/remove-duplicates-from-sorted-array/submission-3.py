class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)-1
        i=n-1
        while i >= 0:
            if nums[i]==nums[n]:
                del nums[n]
            n=i
            i=i-1
        return len(nums)

        