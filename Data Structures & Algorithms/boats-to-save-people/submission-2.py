class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #sort in ascending order
        people.sort()

        n=len(people)
        boats = 0
        i=0
        j=n-1
        while i <= j:
            #pair the lightest with the heaviest
            if i==j:
                boats=boats+1
                break
            weight = people[i]+people[j]

            #if weight exceeds limit, heaviest peson cannot be paired w anyone
            if weight > limit:
                boats=boats+1
                j=j-1
            else:
                i=i+1
                j=j-1
                boats = boats+1
        
        return boats

        