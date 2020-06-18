# class Solution:
#     def longestCommonPrefix(self, strs: []) -> str:
#         if not strs:
#             return "\"\""
#         if len(strs) == 1:
#             return strs[0]
#         for i in range(len(strs[0])-1):
#             try:
#                 for item in strs:
#                     if not item.startswith(strs[0][0:i]):
#                         return strs[0][0:i-1]
#             except:
#                 if i <= 1:
#                     return "\"\""
#                 return strs[0][0:i-1]
#



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i,L in enumerate((*(len(set(t)) for t in zip(*strs)),2)):
            if L>1:return (*strs,"")[0][:i]



if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix([""]))