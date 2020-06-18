class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        news = ''
        while s:
            if len(s) > 2*k:
                news += s[:k][::-1] + s[k:2*k]
                s = s[2*k:]
            elif len(s)>= k:
                news += s[:k][::-1] + s[k:]
                s = None
            else:
                news += s[::-1]
                s = None
        return news


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseStr(s='abcdefg', k=2))