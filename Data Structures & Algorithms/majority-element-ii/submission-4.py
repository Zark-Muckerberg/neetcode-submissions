class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = len(nums)//3
        elements = {}

        for i in nums:
            if i not in elements:
                elements[i]=1
            else:
                elements[i]=elements[i]+1
        
        result = []

        for key in elements:
            if elements[key] > target:
                result.append(key)
        
        return result
        