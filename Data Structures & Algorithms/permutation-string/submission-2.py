class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        #initalise array of character counts for both s1 and s2
        s1Count = {}
        s2Count = {}

        #initalise the character counts for s1
        for char in s1:
            if char in s1Count:
                s1Count[char]=s1Count[char]+1
            else:
                s1Count[char]=1
        
        #initalise character counts for s2 for first window
        for i in range(len(s1)):
            if s2[i] in s2Count:
                s2Count[s2[i]]=s2Count[s2[i]]+1
            else:
                s2Count[s2[i]]=1

        left = 0
        #start from first element outside of window
        for r in range(len(s1),len(s2)):
            if s1Count==s2Count:
                return True
            
            #check if element inside hashMap
            if s2[r] in s2Count:
                s2Count[s2[r]]=s2Count[s2[r]]+1
            else:
                s2Count[s2[r]]=1
            
            #remove the left-most element from the window
            s2Count[s2[left]]=s2Count[s2[left]]-1
            #if count of element is 0, remove from hashMap
            if s2Count[s2[left]]==0:
                del s2Count[s2[left]]
            
            #increment l to point to the new left-most element of window
            left = left+1
        
        return s1Count==s2Count
        

        
        