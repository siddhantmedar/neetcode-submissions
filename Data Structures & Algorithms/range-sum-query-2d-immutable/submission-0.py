class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])
    
    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        res = 0

        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                res+=self.matrix[i][j]    

        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)