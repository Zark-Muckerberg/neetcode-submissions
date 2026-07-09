class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_seen = {}
        t_seen = {}
        n = 0
        x = 0
        if len(s) != len(t):
            return False
        for i in s:
            if i not in s_seen:
                s_seen[i] = 1
            else:
                s_seen[i] = s_seen[i]+1
        for i in t:
            if i not in t_seen:
                t_seen[i]=1
            else:
                t_seen[i]=t_seen[i]+1
        
        return (s_seen == t_seen)


        