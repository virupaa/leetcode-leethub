class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        sum = 0
        for i in hashmap.keys():
            if hashmap[i] == 1:
                sum += i
                
        return sum

    
        
        