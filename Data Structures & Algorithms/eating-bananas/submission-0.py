class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Input- array of integers and a max hours
        Output- Min number with which satisfies max hours condition

        Repeated op- For each possible rate, check total hours to eat
        Search space vvvvv large upto a 1 billion
        Hint- Binary search O(logn)
        """

        min_rate = 1#hours = sum(piles)
        max_rate = max(piles) #hours = len(piles)
        res = max_rate

        while min_rate <= max_rate:
            med_rate = min_rate + (max_rate-min_rate)//2
            hours = sum([math.ceil(p/med_rate) for p in piles]) 

            if hours <= h:
                res = med_rate
                max_rate = med_rate -1

            else:
                min_rate = med_rate + 1

        return res

