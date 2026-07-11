# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        i = 1
        j = n
        
        while True:
            mid = (i+j)//2
            res = guess(mid)
            if res ==1:
                i = mid+1
            elif res==-1:
                j=mid-1
            else:
                return mid


        