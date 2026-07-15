#brute force
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        n=len(s)
        result= 0
        for i in range(n):
            charSet = set()
            for j in range(i,n):
                if s[j] in charSet:
                    break
                else:
                    charSet.add(s[j])
            result = max(result,len(charSet))
        
        return result
            
            


