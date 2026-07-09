class Solution:
    def merge(self,left,right):
        result = []
        i=0
        j=0
        while i < len(left) and j < len(right):
            #compare elements from both lists and append them to result[] in ascending order
            if left[i] <= right[j]:
                result.append(left[i])
                i=i+1
            else:
                result.append(right[j])
                j=j+1
        
        # once all the elements from either left or right have been added to result[], append the rest
        while i < len(left):
            result.append(left[i])
            i=i+1

        while j<len(right):
            result.append(right[j])
            j=j+1
        
        return result


    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        right = nums[mid:]
        left = nums[:mid]
        #recursively sort both halves:
        left_sorted = self.sortArray(left)
        right_sorted = self.sortArray(right)
        
        return self.merge(left_sorted,right_sorted)