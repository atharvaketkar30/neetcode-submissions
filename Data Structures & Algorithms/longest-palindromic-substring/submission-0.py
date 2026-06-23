class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        two pointer/expanding window
        Go outward from each letter
        If any letter makes it non-palindrome, we stop

        for even length palindrome, expand from i and i+1
        for odd, expand from only i

        stopping condition: while letters i and j are same
        """

        resInd = 0
        resLen = 0

        for i in range(len(s)):
            # Odd number of letters
            l , r = i, i
            while l>= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    resLen = r-l+1
                    resInd = l
                l -= 1
                r += 1
                
            
        
            # Even number of letters
            l , r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    resLen = r-l+1
                    resInd = l
                l -= 1
                r += 1
                
            
                

        return s[resInd:resInd+resLen]
