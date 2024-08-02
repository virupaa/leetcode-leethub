class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Initialize a dictionary to count the characters needed
        hashmap = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }
        
        for char in text:
            if char in hashmap:
                hashmap[char] += 1
        
       
        hashmap['l'] //= 2
        hashmap['o'] //= 2
        
        return min(hashmap.values())
            
            

        