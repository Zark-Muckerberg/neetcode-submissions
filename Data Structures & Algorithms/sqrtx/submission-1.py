class Solution:
    def mySqrt(self, x: int) -> int:
        if x <2:
            return x
        i=1
        r = x//2

        while i <= r:

            mid = (i+r)//2

            square = mid * mid

            if square > x:
                r = mid-1
            elif square < x:
                i = mid+1
            else:
                return mid
        #for numbers w non-integer root, r is the largest int whose square does not exceed x
        return r

            
            
        