class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = ""
        for i in range(len(s)):
            if s[i].isalnum():
                res += s[i]
        l,r = 0, len(res) - 1
        while l < r:
            if res[l] != res[r]:
                return False
            l += 1
            r -= 1
        return True
        
    #Can also use regex
    # s = s.lower()
    # string = re.sub("[^A-Za-z0-9]", "", s)
    # i,j = 0, len(string) - 1
    # while i < j:
    #     if string[i] != string[j]:
    #         return False
    #     i += 1
    #     j -= 1
    # return True