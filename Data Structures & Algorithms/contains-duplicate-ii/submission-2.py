class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}
        
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]]=i
            #duplicate found, subtract from index stored from first instance of element
            else:
                check = abs(hashMap[nums[i]]-i)
                #update index in hashMap
                hashMap[nums[i]]=i
                if check <= k:
                    return True
        
        return False