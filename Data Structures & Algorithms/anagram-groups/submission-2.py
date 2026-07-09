class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            # for each string, initialise an array w 26 index, each representing a character
            count = [0]*26

            for i in s:
                #iterating through each character in each string
                #ord in python returns the Unicode value of a single character
                #use ord(i)-ord('a') to get the corresponding value of array index for each char
                count[ord(i)-ord('a')] = count[ord(i)-ord('a')] + 1

            #using the array as key, append the string as corresponding value
            #anagrams will have exact same array configuration
            res[tuple(count)].append(s)
        
        return list(res.values())


        