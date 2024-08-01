class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        for i,j in hashmap.items():
            if j > 1:
                return True
                break
        return False
        



        return False

        