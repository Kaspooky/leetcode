class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {}
        
        dict["I"] = 1
        dict["V"] = 5
        dict["X"] = 10
        dict["L"] = 50
        dict["C"] = 100
        dict["D"] = 500
        dict["M"] = 1000
        value = dict[s[0]]
        for index in range(1,len(s)):
            if dict[s[index]] > dict[s[index-1]]:
                value-= 2*dict[s[index-1]]
                value+= dict[s[index]]
            else:
                value+=dict[s[index]]
        return value
        