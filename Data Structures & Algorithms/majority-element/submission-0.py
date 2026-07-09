class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = {}

        for i in nums:
            if i not in elements:
                elements[i]=0
            else:
                elements[i]=elements[i]+1
        return max(elements,key=elements.get)
        