class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''
        #create new string to remove non-alphanumeric
        for i in s:
            if i.isalnum():
                #remember to convert all to lowercase
                result = result + i.lower()
        i = 0
        j = len(result)-1
        while i<j:
            if result[i]==result[j]:
                i = i+1
                j = j-1
            else:
                return False
        return True
    