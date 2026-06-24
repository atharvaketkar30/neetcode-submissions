class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Minimum number of coins can be reused to calculate higher denom
        To calculate any denom:
        min_coins[denom] = 1 + min(min_coins[denom - coin]) for all coins

        """

        dp = [amount+1]* (amount+1)
        # Base case
        dp[0] = 0
        
        for i in range(1, amount+1):
            min_dp = 10000
            for coin in coins:
                if i - coin >= 0:
                    min_dp = min(dp[i-coin], min_dp)
                # else:
                #     min_dp = -1
            
            dp[i] = 1 + min_dp
        print(dp)
        return dp[-1] if dp[-1] != 10001 else -1