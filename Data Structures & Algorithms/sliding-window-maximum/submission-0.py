class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Input - List of integers upto 100K length and window size
        Output - list of max of each window

        Reprated op- find max of window
        """
        
        out = []
        for l in range(len(nums)-k+1):
            out.append(max(nums[l:l+k]))
        
        return out