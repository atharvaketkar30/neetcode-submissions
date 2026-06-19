class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Input - int n = num steps
        Output - #distinct ways to get sum=n in increments of 1,2
        Repeated op - Repeating pattern and use prev results
            So best for DP
        
        #ways(n) = #ways(n-1) + #ways(n-2) #fibonacci
        Only need prev 2 elems not all before it
        """

        if n==0:
            return 0
        if n == 1:
            return 1

        n_0 = 1
        n_1 = 1
        n_i = 2

        for i in range(2, n+1):
            n_i = n_0 + n_1
            n_0 = n_1
            n_1 = n_i
        
        return n_i

        