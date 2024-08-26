class Solution:
    def reverseWords(self, s: str) -> str:
        cleaned_str = s.split()
        
        return " ".join(reversed(cleaned_str))
        
        
        
        