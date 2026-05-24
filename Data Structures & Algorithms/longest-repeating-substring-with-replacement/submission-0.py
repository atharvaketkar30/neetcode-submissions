class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Input: String and int of max changes
        Output: Int
        Repeated op: check if switched, will it be longest

        Method:
        Brute force: 
        Counter over string:
        s:XYYX then {X:[0,3], Y:[1,2]}, k=2
        If max diff between indices >=k choose max_diff + 1

        AACBABB {A:[0,1,4], B:[3,5,6], C:[2]}, k=1

        Need to check if we can make any of these consecutive 
            with upto k changes

        1. Start from left end l,r
        2. Traverse r thru the array
        3. At each step, leep cntr of historical chars
                Keep track of max frequency as that is our anchor

                while invalid (window length cannot be greater than maxf+k)
                    shrink window, reduce count
                update best window
        """

        seen = {}
        l = 0; changes = 0; maxf = 0; res = 0

        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            maxf = max(maxf, seen[s[r]])
            # Keep track of 
            while (r-l+1) - maxf > k: #while invalid window
                seen[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)

        return res

        