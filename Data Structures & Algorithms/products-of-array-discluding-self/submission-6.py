class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*n
        suffix = [0]*n
        #prefix contains the product of everyth left of an index
        #suffix contains the product of everyth right of an index

        prefix[0]=suffix[n-1]= 1

        for i in range(1,n):
            prefix[i]= prefix[i-1]*nums[i-1]
        
        for j in range(n-2,-1,-1):
            suffix[j]= suffix[j+1]*nums[j+1]
        
        result = [0]*n

        for r in range(n):
            result[r] = prefix[r]*suffix[r]
        
        return result

       

        