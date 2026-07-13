class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        #if array is already in sorted order, the result will be the first element
        result = nums[0]

        while l <= r:
            mid = (l+r)//2
            #if mid is > l, it is in the sorted portion, result lies in right half
            if nums[mid]>=nums[l]:
                result = min(result,nums[l])
                l = mid+1
                
            #mid < l, result is definitely in the left half
            else:
                r = mid-1
                result = min(result,nums[mid])
        
        return result

        

                
                
        