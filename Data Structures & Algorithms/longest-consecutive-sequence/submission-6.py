class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consecutive = set(nums)
        longest = 0

        for n in nums:
            #if n-1 is not in the set, means n is the beginning of the sequence
            if(n-1) not in consecutive:
                length = 0
                #check if consecutive number exists
                while (n+length) in consecutive:
                    length = length+1
                #once sequence ends, compare if this sequence is the longest encountered
                longest = max(length,longest)
        return longest