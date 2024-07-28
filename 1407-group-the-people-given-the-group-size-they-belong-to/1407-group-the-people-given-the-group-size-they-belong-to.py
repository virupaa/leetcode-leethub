class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hashmap = {}
        for i, person in enumerate(groupSizes):
            if person not in hashmap:
                hashmap[person] = [i]
            else:
                hashmap[person].append(i)
       
        res = []
        for i in hashmap:
            
            if len(hashmap[i]) > i:
                temp = hashmap[i]
                for j in range(0,len(temp),i):
                    res.append(temp[j:j+i])
            else:
                res.append(hashmap[i])
        return res
            
        return [[1],[0,5],[2,3,4]]
        


        