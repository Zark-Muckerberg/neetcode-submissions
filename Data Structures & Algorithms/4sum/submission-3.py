class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        results=[]
        nums.sort()
        n=len(nums)

        for i in range(n):
            #duplicate check
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            for j in range(i+1,n):
                #duplicate check
                if j > i+1 and nums[j-1]==nums[j]:
                    continue
                
                k=j+1
                r=n-1

                while k < r:
                    total = nums[i]+nums[j]+nums[k]+nums[r]
                    if total > target:
                        r=r-1
                    elif total < target:
                        k=k+1
                    else:
                        results.append([nums[i],nums[j],nums[k],nums[r]])
                        r=r-1
                        k=k+1
                        #nested while loops to skip duplicate k and r values
                        while k<r and nums[r]==nums[r+1]:
                            r=r-1
                        
                        while k<r and nums[k]==nums[k-1]:
                            k=k+1
        
        return results

                

