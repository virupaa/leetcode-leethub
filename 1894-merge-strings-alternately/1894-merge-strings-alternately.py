class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        a,b = 0,0
        A, B = len(word1), len(word2)
        word = 1
        while a < A and b < B:
            if word == 1:
                res.append(word1[a])
                a += 1
                word = 2
            else:
                res.append(word2[b])
                b += 1
                word = 1
        
        while a < A:
            res.append(word1[a])
            a += 1
        
        while b < B:
            res.append(word2[b])
            b += 1
        
        return ''.join(res)

        
        