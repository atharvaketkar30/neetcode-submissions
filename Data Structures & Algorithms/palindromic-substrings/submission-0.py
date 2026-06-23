class Solution:
    def countSubstrings(self, s: str) -> int:
        
        palin_set = []

        for i in range(len(s)):

            #odd number of letters
            l, r = i, i
            while l>=0 and r<len(s) and s[l]==s[r]:
                palin_set.append(s[l:r+1])
                l -= 1
                r += 1

            #even number
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                palin_set.append(s[l:r+1])
                l -= 1
                r += 1
        
        return len(palin_set)