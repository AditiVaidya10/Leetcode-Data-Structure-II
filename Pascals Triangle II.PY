class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1 for _ in range(rowIndex + 1)]
        
        for i in range(1, rowIndex + 1):
            row[i] = int(row[i-1] * (rowIndex - i + 1) / i)
        
        return row
