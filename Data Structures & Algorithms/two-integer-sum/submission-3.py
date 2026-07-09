class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}

        n= len(nums)
        for i in range(n):
            remainder = target - nums[i]
            if remainder not in complement:
                complement[nums[i]]=i
            else:
                return [complement[remainder],i]

        