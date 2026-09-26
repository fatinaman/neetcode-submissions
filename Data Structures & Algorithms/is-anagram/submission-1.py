class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s, hash_t = {}, {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                hash_s[s[i]] = 1 + hash_s.get(s[i],0)
                hash_t[t[i]] = 1 + hash_t.get(t[i],0)
            for char in s:
                if hash_s[char] != hash_t.get(char,-1):
                    return False
            return True
        