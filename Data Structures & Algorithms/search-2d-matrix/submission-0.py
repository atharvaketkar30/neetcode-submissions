class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Input- Sorted 2D matrix
        Output- if target exists
        Repeated op- Scnanning elements

        Since it is sorted, we can exploit structure
        1> See if element can exist in row, leftmost <=target <= rightmost
        2> If no, next row, if yes Binary search
        """

        n_r = len(matrix)
        n_c = len(matrix[0])

        for r in range(n_r):
            if matrix[r][0] <= target <= matrix[r][n_c-1]:
                l = 0
                ri = n_c-1
                while l <= ri:
                    mid = l + (ri-l)//2
                    if matrix[r][mid] == target:
                        return True
                    elif matrix[r][mid] > target:
                        ri = mid-1
                    else:
                        l = mid+1
        return False
