class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        prevMap = {}
        for i in range(len(s)):
            prevMap[s[i]] = prevMap.get(s[i], 0) + 1

        for j in range(len(t)):
            if t[j] not in prevMap:
                return False
            prevMap[t[j]] -= 1
            if prevMap[t[j]] < 0:
                return False
        return True

