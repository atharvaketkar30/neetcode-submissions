class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Given a square, we can say how many ways to get to bottom-right
        dp[i][j] = num paths from bottom or right square
                = dp[i+1][j] + dp[i][j+1]

        """

        dp = [[0]*n for _ in range(m)]

        dp[m-1][n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i < m-1 and j < n-1:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
                elif i < m-1:
                    dp[i][j] = dp[i+1][j]
                elif j < n-1:
                    dp[i][j] = dp[i][j+1]
                else:
                    dp[i][j] = 1
        
        return dp[0][0]

