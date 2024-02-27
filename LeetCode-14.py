class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        comPfx = ""
        string = min(strs, key=len)
        for index, letter in enumerate(string):
            # print(index, " ", letter)
            for strings in strs:
                if strings[index] != letter:
                    return comPfx
            comPfx += letter
            if len(string) == len(comPfx):
                return comPfx
        return comPfx
