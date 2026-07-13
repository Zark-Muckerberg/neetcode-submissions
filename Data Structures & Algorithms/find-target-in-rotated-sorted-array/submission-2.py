class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums)-1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid

            #if l up to mid is sorted
            if nums[l] <= nums[mid]:
                #left half is sorted, if target is between l and m it must be here
                if nums[l]<=target and target < nums[mid]:
                    r = mid-1
                #target is in the right half
                else:
                    l = mid +1
            #not sorted, see if target lies between mid and r
            else:
                #target lies within right sorted array
                if target > nums[mid] and target <= nums[r]:
                    l = mid+1
                #target is in the left unsorted portion
                else:
                    r = mid-1
        
        return -1


        