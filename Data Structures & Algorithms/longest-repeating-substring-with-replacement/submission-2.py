class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        count = {}
        res = 0
        freqmax = 0
        for j in range(len(s)):
            count[s[j]] = count.get(s[j], 0) + 1
            freqmax = max(freqmax, count[s[j]])
            if j - i + 1 - freqmax > k :
                count[s[i]] -= 1
                i += 1
            res = max(res, j-i + 1)
        return res
                


            
                