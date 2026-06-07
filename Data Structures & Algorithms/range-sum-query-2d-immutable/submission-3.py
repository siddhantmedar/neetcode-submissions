class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        self.m = len(matrix)
        self.n = len(matrix[0])
        
        self.prefix = [[0]*self.n for _ in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                if i==0 and j==0:
                    self.prefix[i][j] += self.matrix[i][j]

                elif i==0 and j>0: self.prefix[i][j] += self.prefix[i][j-1] + self.matrix[i][j]
                elif j==0 and i>0: self.prefix[i][j] += self.prefix[i-1][j] + self.matrix[i][j]
                else: self.prefix[i][j] += self.prefix[i-1][j]+self.prefix[i][j-1]-self.prefix[i-1][j-1] + self.matrix[i][j]
    
    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return self.prefix[r2][c2] -(self.prefix[r2][c1-1] if c1-1>=0 else 0)- (self.prefix[r1-1][c2] if r1-1>=0 else 0) + (self.prefix[r1-1][c1-1] if r1-1>=0 and c1-1>= 0 else 0)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)