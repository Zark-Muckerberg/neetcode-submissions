class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        self.prefix = []
        #populate the prefix sum matrix w all zeros, extra row and column of 0s to prevent index out of range
        for i in range(row+1):
            rows = [0]* (col+1)
            self.prefix.append(rows)
        #build the 2D prefix matrix; each square contains the sums of all values from top left square to it
        for r in range(row):
            for c in range(col):
                self.prefix[r+1][c+1]= self.prefix[r+1][c]+self.prefix[r][c+1] + matrix[r][c] - self.prefix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        return(self.prefix[row2+1][col2+1]+self.prefix[row1][col1]-self.prefix[row1][col2+1]-self.prefix[row2+1][col1])
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)