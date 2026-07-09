class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        for a in asteroids:
            #if stack is non empty, next asteroid is moving left, and prev asteroid moving right
            while stack and a < 0 and stack[-1]>0:
                if abs(a) > stack[-1]:
                    #left bigger than right, destroy right
                    stack.pop()
                elif abs(a)<stack[-1]:
                    #if right bigger than left, left is destroyed. destroy it by setting to 0
                    a=0
                else:
                    #left right equal, destroy both
                    a=0
                    stack.pop()
            #if no collision, we add to stack. "destroyed" asteroids set to 0, do not add those
            if a !=0:
                stack.append(a)

        return stack
            
            


        