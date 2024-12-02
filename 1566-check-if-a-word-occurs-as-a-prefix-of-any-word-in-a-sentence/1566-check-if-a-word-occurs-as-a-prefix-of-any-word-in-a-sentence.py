class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sent = sentence.split(" ")
        len_search = len(searchWord)

        for i,word in enumerate(sent):
            if word.startswith(searchWord):
                return i + 1
           

        
        return -1

        