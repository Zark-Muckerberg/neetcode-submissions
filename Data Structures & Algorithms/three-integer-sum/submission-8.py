class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the array in increasing order first
        nums.sort() #O(nlogn)
        n = len(nums)
        i=0
        result=[]
        #i tracks the candidate element, j and k tracks if there is a possible pair + i that sums up to 0
        
        for i in range(n):

            #check if i-th element is not a duplicate
            if i > 0 and nums[i] == nums[i-1]:
                #if it is a duplicate, skip to next iteration
                continue
            
            j=i+1
            k=n-1
            #2 pointer method
            while j < k:
                total = nums[i]+nums[j]+nums[k]
                if total < 0:
                    j=j+1
                elif total >0:
                    k=k-1
                else:
                    result.append([nums[i],nums[j],nums[k]])
                    j=j+1
                    k=k-1
                    #duplicate check
                    while j < k and nums[j-1]==nums[j]:
                        j=j+1
                    while j<k and nums[k]==nums[k+1]: 
                        k=k-1
        return result




            