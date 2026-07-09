class Solution:
    
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_ptr = 0
        n = len(nums)
        two_ptr = n-1
        i=0
        while i<=two_ptr:
            #initialise zero ptr at start of array and two ptr at end of array
            #if nums[i] is 0,swap it with the element at nums[zero_ptr]
            if nums[i]==0:
                nums[zero_ptr],nums[i]=nums[i],nums[zero_ptr]
                #element at nums[zero_ptr] is confirmed to be 0, we increment zero_ptr by 1
                zero_ptr = zero_ptr + 1
                #if nums[i] is 0,swap it with the element at nums[two_ptr]
                i=i+1
            elif nums[i]==2:
                nums[two_ptr],nums[i]=nums[i],nums[two_ptr]
                #element at two_ptr confirmed to be 2, we decrement two_ptr by 1
                two_ptr = two_ptr-1
            else:
                i=i+1
            
            
            
            