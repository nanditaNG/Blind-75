class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashOne = {}
        hashTwo = {}
        s = sorted(s)
        t = sorted(t)
        for char in s:
            if char not in hashOne:
                hashOne[char] = 1
            hashOne[char] += 1
        for char in t:
            if char not in hashTwo:
                hashTwo[char] = 1
            hashTwo[char] += 1
        if hashOne == hashTwo:
            return True
        return False