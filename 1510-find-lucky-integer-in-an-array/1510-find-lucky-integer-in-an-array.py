class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = {}
        count = 0
        res = []
        for i in arr:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
       
        for i,j in hashmap.items():
            
            if i == j:
                res.append(i)
       
        if len(res) > 0:
            return max(res)
        else:
            return -1
        
            
            
        

        