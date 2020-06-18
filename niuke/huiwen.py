# import math
#
# # s = "goofadsafaogle"
# # s = "aba"
# s = input()
#
#
# def deleteOne(ss,num):
#     news = []
#     for s in ss:
#         for i in range(0, len(s)):
#             news.append(s[0:i] + s[i + 1:])
#     if checkBack(news):
#         return (num + 1)
#     else:
#         return deleteOne(news,num+1)
#
#
#
# def checkBack(ss):
#     for s in ss:
#         if s[0:math.ceil(len(s)/2)] == s[::-1][0:math.ceil(len(s)/2)]:
#             return 1
#     return 0
#
# if __name__ == '__main__':
#     if checkBack([s]):
#         print(0)
#     else:
#         num = deleteOne([s],0)
#         print(num)




# s = input()
#
#
# def deleteOne(ss,num):
#     news = []
#     for s in ss:
#         for i in range(0, len(s)):
#             news.append(s[0:i] + s[i + 1:])
#     if checkBack(news):
#         return (num + 1)
#     else:
#         return deleteOne(news,num+1)
#
#
#
# def checkBack(ss):
#     for s in ss:
#         if s[0:-(-len(s)//2)] == s[::-1][0:-(-len(s)//2)]:
#             return 1
#     return 0
#
# if __name__ == '__main__':
#     if checkBack([s]):
#         print(0)
#     else:
#         print(deleteOne([s],0))


import sys

def maxlcp(strs):
    if strs == None or len(strs) == 0:
        return 0
    lens = len(strs)
    dp = [0] * lens
    dp[0] = 1 if strs[0] == strs[lens - 1] else 0
    for i in range(lens):
        pre = dp[0]
        dp[0] = max(dp[0], 1 if strs[i] == strs[lens - 1] else 0)
        for j in range(1, lens):
            cur = dp[j]
            dp[j] = max(dp[j], dp[j - 1])
            if strs[i] == strs[lens - 1 - j]:
                dp[j] = max(dp[j], pre + 1)
            pre = cur

    return dp[lens - 1]


if __name__ == '__main__':
    while True:
        line = sys.stdin.readline().strip()
        lens = len(line)
        if not line:
            break
        maxLcp = maxlcp(line)
        # if maxLcp == 1:
        #     print(0)
        # else:
        #     print(maxLcp)
        print(lens - maxLcp)