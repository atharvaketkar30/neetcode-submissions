class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Initialze a set 
        Method 1 : Check if len of array = len of set of array
        If duplicates, then set will be smaller

        Method 2:
            Initialize set
            traverse the array and check if number already in set, return True
            If not in set add to set
            If no true returned return False
        """
        hashset = set()

        for i, n in enumerate(nums):
            if n in hashset:
                return True
            else:
                hashset.add(n)

        return False        