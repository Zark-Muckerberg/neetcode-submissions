class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        #2D array of each car's position and velocity
        cars = []

        for p,v in zip(position,speed):
            cars.append((p,v))
        #sort in descending order based on position, as cars cant be overtaken, process by closest car to target first
        cars.sort(reverse = True)
        stack = []
        #for each car, calculate the time it needs to get to target
        for p,v in cars:
            time = (target - p)/v
            #if stack not empty, we compare the time a car takes vs the car that is ahead of it
            #if that car is faster, it will join the car ahead and form a fleet
            if stack and time <= stack[-1]:
                #if i+1-th car is faster than i-th car, it will meet up and slow down
                #we do not need to add the faster car to the stack
                continue
            else:
                #i+1th car will never meet with i-th car, separate fleets, append to stack
                stack.append(time)

        return len(stack)


        
        