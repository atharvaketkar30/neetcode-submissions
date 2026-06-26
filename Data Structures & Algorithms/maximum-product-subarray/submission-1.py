class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Input- integers, can be negative, max len 1000
        Contiguous subarray- Sliding window
            But -ve numbers so logic will break
            if 2 ive nums then product will be +ve


        Start from left most
        Keep track of max product up until i, min prod up until i as well
            Becasue if nums[i] is -ve and min_prod -ve, then prod is +ve
            candidates = nums[i], min_prod*nums[i], max_prod*nums[i]

        """

        result, min_prod, max_prod = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            candidates = (nums[i], min_prod*nums[i], max_prod*nums[i])

            min_prod = min(candidates)
            max_prod = max(candidates)

            result = max(result, max_prod) # If incl nums[i] reduces product then result
        return result
        # return max(dp)