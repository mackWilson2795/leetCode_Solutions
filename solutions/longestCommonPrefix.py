class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        pref = min(strs, key=len)
        for s in strs:
            for i, c in enumerate(pref):
                if c != s[i]:
                    pref = s[:i]
                    break
            if pref == "":
                return ""
        return pref