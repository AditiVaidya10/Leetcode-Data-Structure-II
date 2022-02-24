class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        H = len(matrix)
        W = len(matrix[0])
        for row in range(H):
            low, high = 0, W - 1
            while low <= high:
                mid = (high + low) // 2
                if target == matrix[row][mid]:
                    return True
                elif target < matrix[row][mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return False
