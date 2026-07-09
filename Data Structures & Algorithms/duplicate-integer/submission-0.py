class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i in nums:
            if i not in seen:
                seen[i]=True
            else:
                return True
        return False
        