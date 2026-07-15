#sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #map to store last index of each character
        mp = {}
        #for longest length
        result = 0
        #l for start of window
        l=0

        for i in range(len(s)):
            if s[i] in mp:
                l = max(mp[s[i]]+1,l)

            mp[s[i]] = i
            result = max(result,i-l+1)
        
        return result
        