class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l < r:
            #if l+r too big, decrease r:
            if numbers[l]+numbers[r]>target:
                r=r-1
            #if l+r too small, increase l:
            elif numbers[l]+numbers[r]<target:
                l=l+1
            #equal to target
            else:
                return [l+1,r+1]
        