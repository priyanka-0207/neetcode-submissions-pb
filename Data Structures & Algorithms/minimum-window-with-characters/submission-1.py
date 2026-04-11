class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = {}
        window = {}
        have, need  = 0, 0
        best = float("inf")
        res = [-1, -1]
        i = 0
        for j in range(len(t)):
            freq_t[t[j]] = freq_t.get(t[j], 0) + 1
        need = len(freq_t)
        for j in range(len(s)):
            window[s[j]] = window.get(s[j], 0) + 1
            if s[j] in freq_t and window[s[j]] == freq_t[s[j]]:
                have += 1
            while have == need:
                if (j - i + 1) < best:
                    best =  j - i + 1
                    res = [i, j]
                window[s[i]] -= 1
                if s[i] in freq_t and window[s[i]] < freq_t[s[i]]:
                    have -= 1
                i += 1 
        l, r = res
        return s[l:r+1] if best != float("inf") else ""

        