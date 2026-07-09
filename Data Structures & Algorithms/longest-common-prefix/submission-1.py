class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)

        n = len(strs[0])

        prefix={}
        for i in range(n):
            for j in strs:
                if j[i]!= strs[0][i]:
                    return j[0:i] 
        return strs[0]

