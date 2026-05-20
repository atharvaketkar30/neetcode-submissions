class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Input- List of integers

        Output- Max profit integer

        Doing repeatedly- Checking max value to the right

        No fluff- Find the largest diff between a number and highest value to its right

        Method:
        1)Maintain two pointers
            One buy and one sell (sell > buy)
        2) Keep a running track of highest profit yet
        3) 

        """
        # maxP = 0

        # for i in range(len(prices)-1):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         maxP = max(maxP, profit)
        
        # return max(maxP, 0)

        # right = [0]*len(prices)
        # rMax = 0
        # for i in range(len(prices)-2, -1, -1):
        #     rMax = max(rMax, prices[i+1])
        #     right[i] = rMax
        
        # profits = [right[i] - prices[i] for i in range(len(prices))]
        # print(right, profits)
        # return max(max(profits), 0)

        buy = 0; sell = 1
        maxP = 0
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                maxP = max(maxP, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        return maxP

        