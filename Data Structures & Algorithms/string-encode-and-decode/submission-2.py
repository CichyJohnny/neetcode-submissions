class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(str(len(s)) + "#" + s)
        return "".join(result)

# ["a", "bc", "def"]
# "1#a|2#bc|3#def"
# [""]
# "0#|"
# ["", ""]
# "0#|0#|"
# ["a ", " ", "a"]
# "2#a |1# |1#a|"

    def decode(self, s: str) -> List[str]:
        print(s)
        results = []
        curr_num = ""
        count_phase = True
        for ss in s:
            if count_phase and ss == "#":
                count_phase = False
                curr_num = int(curr_num)
                results.append("")
                if curr_num > 0:
                    continue
                else:
                    curr_num = ""
                    count_phase = True
                    continue

            if count_phase:
                curr_num += ss
                continue
            
            results[-1] += ss
            curr_num -= 1
            if curr_num == 0:
                curr_num = ""
                count_phase = True


        return results

        
