class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        seen = set()

        def two_sum(start, target):
            ts_tuple = set()
            for i in range(start, len(nums)):
                if target-nums[i] in ts_tuple:
                    seen.add(tuple(sorted([-target, nums[i], target-nums[i]])))
                ts_tuple.add(nums[i])

            # return ts_tuple

        # seen = set()# {0:[0], 2:[1,3], 3:[2]}
        for i in range(len(nums)):
            target = -nums[i]
            two_sum(i+1, target)
            # seen.add([i, j, k for (j,k) in seen_two])
        return([list(t) for t in seen])