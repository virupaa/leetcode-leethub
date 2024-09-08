class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append("")

        res_index = 0
        cur_char = ""
        cur_num = 0

        for c in chars:
            if not cur_char:
                cur_char = c
                cur_num = 1
            elif c != cur_char:
                chars[res_index] = cur_char
                res_index += 1
                if cur_num > 1:
                    for num_str in str(cur_num):
                        chars[res_index] = num_str
                        res_index += 1
                cur_char = c
                cur_num = 1
            else:
                cur_num += 1

        return res_index