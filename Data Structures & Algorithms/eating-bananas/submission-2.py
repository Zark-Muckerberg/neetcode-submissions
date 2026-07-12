class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #h must be equal to the length of the list, for it to be possible to finish eating within h
        right = max(piles)
        left = 1
        min_k = 10000

        while left <= right:
            hours = 0
            mid = (left+right)//2

            for i in piles:
                time = math.ceil(i/mid)
                hours = hours + time
            
            #too slow, need to increase banana eating rate
            if hours > h:
                left = mid +1
            #fast enough, see if we can do better
            else:
                min_k = mid
                right = mid -1
        
        return min_k
