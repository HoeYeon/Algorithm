class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = start = 0
        d = {}
        for i, v in enumerate(s):
            if v in d:
                start = max(d[v]+1, start)
            ans = max(i-start + 1, ans)
            d[v] = i

        return ans
