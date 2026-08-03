class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}

        if len(s) != len(t):
            return False

        for char in s:
            freq_s[char] = freq_s.get(char,0) + 1
        
        for char in t:
            freq_s[char] = freq_s.get(char,0) - 1

        
        for value in freq_s.values():
            if value != 0:
                return False

        return True
