class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        newStr = ''
        n = len(word1)
        m= len(word2)
        i=0
        j=0

        while i<n or j<m:
            if i<n:
                newStr = newStr + word1[i]
            if j<m:
                newStr = newStr + word2[j]
            i = i+1
            j=j+1
        return newStr

        