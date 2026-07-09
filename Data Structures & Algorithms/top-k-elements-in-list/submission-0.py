class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        for i in nums:
            if i not in elements:
                elements[i]=1
            else:
                elements[i]= elements[i]+1
        
        candidates = []
        for i in range(k):
            candidates.append(max(elements,key=elements.get))
            elements[candidates[i]]=0
        return candidates