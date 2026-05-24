class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Input- two strings lowercase letters
        Output- True if s2 contains perm(s1) else False

        Repeated op: check if len(s1) chars of s2 are perm(s1)
            Fixed window sliding over s2

        Method:
        To check if two strings are a permutation-
            Counter over both = same

        1. start with base counter over first len(s1) chars of s2
        2. traverse with removing l and adding r to window
        """

        from collections import Counter

        def is_permutation(s,t):
            return Counter(s) == Counter(t)

        n = len(s1)
        m = len(s2)
        base = Counter(s1)

        comp_str = s2[:n]
        comp_cntr = Counter(comp_str)

        if m<n:
            return False
        if base == comp_cntr:
            return True

        for l in range(0, m-n):
            comp_cntr[s2[l]] -= 1
            comp_cntr[s2[l+n]] = comp_cntr.get(s2[l+n], 0) + 1
            if base == comp_cntr:
                return True
            
        
        return False
            



        