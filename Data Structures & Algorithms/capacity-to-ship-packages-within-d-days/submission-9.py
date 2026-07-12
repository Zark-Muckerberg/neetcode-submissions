class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #if not we wont be able to load the cargo
        min_capacity = max(weights)
        #to load everything in one day
        max_capacity = sum(weights)

        while min_capacity <= max_capacity:
            target = (min_capacity+max_capacity)//2
            #k is the number of days needed to ship all packages within days
            k = 1
            i=0
            leftover = target

            while i < len(weights):
                #if we have leftover capacity, save it for next package
                if leftover - weights[i] > 0:
                    leftover = leftover - weights[i]
                    i=i+1
                #insufficient capacity, ship previous load as 1 day, load current as new day
                elif leftover - weights[i] <0:
                    k = k +1
                    leftover = target
                else:
                    leftover = target
                    i = i+1
                    #add a day only if packages remain
                    if i < len(weights):
                        k = k+1
            #after while loop exits, we know the k days for a given target capacity
            #if k is lesser than days, our current capacity could be too high
            if k <= days:
                max_capacity= target-1
            #takes too long, need to increase target
            if k> days:
                min_capacity = target+1   

        return min_capacity


            


