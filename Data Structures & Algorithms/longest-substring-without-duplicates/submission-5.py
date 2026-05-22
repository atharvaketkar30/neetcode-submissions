class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Input = string of len <= 1000
        Output = longest substr w/o repetition

        Method=
        Initialize a seen dict storing index of chars seen
        1. Start at left and keep expanding window to right till not end
        2. If r is a new char, add to res
            else if r in seen, bring l to where first seen
        3. Keep updating max and return length
        """

        if s == "":
            return 0

        seen = {}
        l = 0
        maxL = 0

        for r in range(len(s)):
            if s[r] in seen:
                l = max(l, seen[s[r]] + 1) #need to take max as seen[s[r]] can be before l also
                # l = seen[s[r]] + 1
            
            seen[s[r]] = r
            maxL = max(maxL, r-l+1)

        return maxL

    
        