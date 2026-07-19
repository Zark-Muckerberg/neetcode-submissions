class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i in range(len(nums)-k+1):
            largest = float('-inf')
            for j in range(i,i+k):
                if nums[j]>largest:
                    largest = nums[j]
            result.append(largest)
        
        return result
        