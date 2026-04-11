class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        i = 0
        count = {}
        res = 0
        win_size = 0
        for j in range(len(s)):
            count[s[j]] = count.get(s[j], 0) + 1
            win_size = j - i + 1 
            max_freq = max(max_freq, count[s[j]])
            if win_size - max_freq  > k:
                count[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        return res

            
                