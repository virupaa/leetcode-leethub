class Solution:
    def stringSequence(self, target: str) -> List[str]:
        result = []
        string = ""

        for i, char in enumerate(target):
            string += "a"
            result.append(string)

            while string[-1] != char:
                string = string[:-1] + chr(ord(string[-1]) + 1)
                result.append(string)
        return result


        