class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Input- List of integers

        Output- Max profit integer

        No fluff- Find the largest diff between a number and highest value to its right

        Method:
        1)Maintain two pointers
            One buy and one sell (sell > buy)
        2) Keep a running track of highest profit yet
        3) 

        """
        maxP = 0

        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                maxP = max(maxP, profit)
        
        return max(maxP, 0)

        