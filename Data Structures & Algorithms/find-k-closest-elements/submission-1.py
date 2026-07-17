class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        l=0
        r=len(arr)-k

        while l < r:
            #mid represents the left-most value of window
            mid = (l+r)//2
            #if the left-most element is further from target than first element to the right of window
            if x-arr[mid] > arr[mid+k] - x:
                #shift the window to the right
                l = mid +1
            #else, no need to go any further to the right
            else:
                r = mid
        #return starting from element l up to l+k
        return arr[l:l+k]


        