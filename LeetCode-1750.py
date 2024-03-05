# # ORIGINAL SOLUTION : RECURSION
# class Solution:
#     def minimumLength(self, s: str) -> int:
#         val = len(s)

#         # base cases
#         if val == 1 or val == 0:
#             return val

#         if s[0] != s[-1]:
#             return val

#         # recursion function
#         char = s[0]
#         prefixIndex = 0
#         suffixIndex = -1

#         while True:
#             if s[prefixIndex+1] == char:
#                 prefixIndex += 1
#                 continue
#             else:
#                 break
#         print()
#         while True:
#             if s[suffixIndex-1] == char:
#                 suffixIndex -= 1
#                 continue
#             else:
#                 break
#         answer = Solution.minimumLength(self, s=s[prefixIndex:suffixIndex])
#         return answer


# value = Solution
# ret = value.minimumLength(s="cabaabac")
# print(value)


def minimumLength(s: str):
    char = s[0]
    suffixIndex = len(s) - 1
    prefixIndex = 0

    if s[0] != s[-1]:
        return len(s)
    for num in range(1, int(len(s)/2)):
        if s[num] != char:
            if s[suffixIndex] != char:
                return len(s[prefixIndex:suffixIndex])


print(minimumLength("ccabaabac"))
