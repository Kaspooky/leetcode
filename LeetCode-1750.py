# ORIGINAL SOLUTION : RECURSION
class Solution:
    def minimumLength(self, s: str) -> int:
        val = len(s)

        # base cases
        if val == 1 or val == 0:
            return val

        if s[0] != s[-1]:
            return val

        # recursion function
        char = s[0]
        prefixIndex = 0
        suffixIndex = -1

        while True:
            if s[prefixIndex+1] == char:
                prefixIndex += 1
                continue
            else:
                break
        print()
        while True:
            if s[suffixIndex-1] == char:
                suffixIndex -= 1
                continue
            else:
                break
        answer = Solution.minimumLength(self, s=s[prefixIndex:suffixIndex])
        return answer


value = Solution
ret = value.minimumLength(s="cabaabac")
print(value)
